import sys
import os
# Ensure project root is on sys.path so `backend` package can be imported
sys.path.insert(0, os.getcwd())

from backend.app import splunk_client as s

print('using_sample_data=', s.using_sample_data())
print('--- fetch_alert ---')
try:
    a = s.fetch_alert('alert-001')
    print(a)
except Exception as e:
    import traceback
    traceback.print_exc()

print('\n--- search_logs ---')
try:
    r = s.search_logs('index=* "failed login"')
    print('results count=', len(r))
    if r:
        print(r[0])
except Exception as e:
    import traceback
    traceback.print_exc()
