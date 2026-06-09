#!/usr/bin/env python3
import importlib.util
import sys
import os
import traceback

ROOT = os.path.dirname(__file__)
TEST_PATH = os.path.join(ROOT, "lib", "testing", "song_test.py")

# ensure lib is on sys.path so 'from song import Song' works
sys.path.insert(0, os.path.join(ROOT, "lib"))
spec = importlib.util.spec_from_file_location("song_test", TEST_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules["song_test"] = mod
try:
    spec.loader.exec_module(mod)
except Exception:
    print("FAILED: error importing test module")
    traceback.print_exc()
    sys.exit(2)

TestSong = getattr(mod, "TestSong", None)
if TestSong is None:
    print("No TestSong class found in test module")
    sys.exit(1)

instance = TestSong()
failed = []
for name in dir(TestSong):
    if name.startswith("test_"):
        func = getattr(instance, name)
        try:
            func()
            print(f"PASS {name}")
        except AssertionError:
            print(f"FAIL {name}: AssertionError")
            failed.append(name)
        except Exception:
            print(f"ERROR {name}: Unexpected exception")
            traceback.print_exc()
            failed.append(name)

if failed:
    print(f"{len(failed)} tests failed: {failed}")
    sys.exit(1)
else:
    print("All tests passed")
    sys.exit(0)
