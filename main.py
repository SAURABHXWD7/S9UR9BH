import platform
import sys

arch = platform.machine()
if arch not in ("aarch64", "arm64"):
    print("❌ Ye tool sirf ARM64 devices ke liye build hai")
    print("Your architecture:", arch)
    sys.exit(1)

try:
    import S9UR9BH_XD
except ImportError as e:
    print("❌ Module load nahi ho pa raha!")
    print("Reason:", e)
    print("\nFix:")
    print("1) Python version 3.12 hona chahiye")
    print("2) Termux ARM64 device hona chahiye")
    print("3) .so file isi folder me ho")
    sys.exit(1)

# Entry function call
if hasattr(S9UR9BH_XD, "comment"):
    S9UR9BH_XD.comment()
elif hasattr(S9UR9BH_XD, "main"):
    S9UR9BH_XD.main()
else:
    print("⚠️ Module load ho gaya, lekin koi callable function nahi mila")
    print("Available functions:", dir(S9UR9BH_XD))
