#!/usr/bin/env python3
"""
sage_discovery.py — Figure out WHICH Sage USC runs and what you can integrate with,
BEFORE committing to a connector design. Read-only, non-destructive.

Run this once you have any access (or run pieces of it with USC IT in the room).
It does not modify anything. It only inspects and reports.

Usage:
    python sage_discovery.py            # interactive: walks you through identification
    python sage_discovery.py --probe-sql "DRIVER=...;SERVER=...;DATABASE=...;UID=...;PWD=..."
"""
import sys, os, json, datetime

REPORT = {}

SAGE_FINGERPRINTS = {
    "Sage Estimating (Timberline)": {
        "signals": [
            "Desktop app: 'Sage Estimating' or 'Sage Timberline Office' / 'Sage 300 CRE'",
            "Data store: Pervasive PSQL / Btrieve (.btr files) OR Microsoft SQL Server",
            "Estimate DB tables often prefixed or grouped under an 'Estimating' catalog",
            "Files with .pei / .est extensions, or a 'Sage Estimating' SQL instance",
        ],
        "integration_surface": "NO public REST API. Options: read the SQL Server DB "
            "directly (newer installs), ODBC against Pervasive (older), or Sage's "
            "Estimating SDK / Office Connector. Read-only strongly preferred.",
        "realistic_play": "Read estimate headers, cost items, and totals from a SQL "
            "replica or read-replica. NEVER write to estimating tables.",
    },
    "Sage Intacct": {
        "signals": [
            "Cloud login at *.intacct.com",
            "Talk of 'dimensions', 'GL', 'AP/AR' rather than takeoffs/assemblies",
            "It's accounting/financials, not estimating per se",
        ],
        "integration_surface": "REAL web API (XML/REST-ish 'Web Services' + newer REST). "
            "OAuth/sender-id + credentials. This one is genuinely API-able.",
        "realistic_play": "Pull financial actuals to compare against estimates. Clean API. "
            "Read scope first; write only to custom objects you own.",
    },
    "Sage 100/300 Construction & Real Estate (CRE)": {
        "signals": [
            "On-prem ERP; modules like Job Cost, Project Management, Accounts Payable",
            "Backed by Pervasive PSQL historically; some on MS SQL",
            "Often the system Estimating *feeds into* after a bid is won",
        ],
        "integration_surface": "Limited. ODBC read via the Sage data sources; the "
            "'Sage Office Connector' (Event/Query/Write) is the sanctioned path but "
            "is itself a paid add-on. No modern REST API.",
        "realistic_play": "Read job cost actuals via ODBC for analysis. Writes go through "
            "Office Connector Write with controls, if at all.",
    },
}

def banner(t): print("\n" + "="*68 + f"\n{t}\n" + "="*68)

def identify():
    banner("STEP 1 — Identify which Sage USC runs")
    print("Answer from what you can see, or take these questions to USC IT.\n")
    qs = [
        ("What's the app icon/title on an estimator's desktop?",
         "e.g. 'Sage Estimating', 'Sage Timberline Office', 'Sage 300 CRE', or a browser tab"),
        ("Is it a desktop program or a website (*.intacct.com)?",
         "desktop => Estimating/CRE; website => Intacct"),
        ("Where does the data live, if anyone knows?",
         "'SQL Server', 'Pervasive/PSQL/Btrieve', or 'it's in the cloud'"),
        ("What does the estimating team call their files/outputs?",
         "spreadsheets exported? .est/.pei files? a shared SQL db?"),
    ]
    answers = {}
    for q, hint in qs:
        print(f"\n• {q}\n  ({hint})")
        answers[q] = input("  > ").strip()
    REPORT["identification"] = answers
    print("\nLikely matches based on your answers:")
    blob = " ".join(answers.values()).lower()
    for name, fp in SAGE_FINGERPRINTS.items():
        score = sum(1 for s in fp["signals"] if any(
            w in blob for w in s.lower().split() if len(w) > 4))
        if score:
            print(f"  - {name}  (signal hits: {score})")
    return answers

def show_surfaces():
    banner("STEP 2 — What integration is actually possible per product")
    for name, fp in SAGE_FINGERPRINTS.items():
        print(f"\n### {name}")
        print(f"  Surface:  {fp['integration_surface']}")
        print(f"  Best play: {fp['realistic_play']}")

def probe_sql(conn_str):
    banner("STEP 3 — Read-only SQL probe (non-destructive)")
    try:
        import pyodbc
    except ImportError:
        print("pyodbc not installed. Run: pip install pyodbc --break-system-packages")
        return
    try:
        cx = pyodbc.connect(conn_str, timeout=10, readonly=True)
        cur = cx.cursor()
        print("Connected. Listing tables (read-only)...")
        tables = []
        for row in cur.tables(tableType="TABLE"):
            tables.append(row.table_name)
        REPORT["sql_tables"] = tables
        print(f"  Found {len(tables)} tables.")
        est_like = [t for t in tables if any(k in t.lower()
                    for k in ("estimat", "bid", "cost", "item", "job", "takeoff", "assembl"))]
        print("  Estimate-relevant candidates:")
        for t in est_like[:40]:
            print(f"    - {t}")
        cx.close()
    except Exception as e:
        print(f"  Probe failed (this is fine during discovery): {e}")

def write_report():
    REPORT["generated"] = datetime.datetime.now().isoformat()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sage_discovery_report.json")
    with open(out, "w") as f:
        json.dump(REPORT, f, indent=2)
    print(f"\nSaved report -> {out}")
    print("Hand this to Claude Code (and optionally USC IT) to scope the real connector.")

if __name__ == "__main__":
    if "--probe-sql" in sys.argv:
        probe_sql(sys.argv[sys.argv.index("--probe-sql")+1])
    else:
        identify()
        show_surfaces()
    write_report()
