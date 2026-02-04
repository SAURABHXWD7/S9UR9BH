import sys

try:
    import S9UR9BH_XD
except ImportError as e:
    print("❌ Module load nahi ho pa raha!")
    print("Reason:", e)
    print("\nEnsure karo ki:")
    print("1. .so file isi folder me ho")
    print("2. Python version same ho (cp312)")
    print("3. Architecture ARM64 ho")
    sys.exit(1)

# Agar tumhare module me main() ya comment() function hai
if hasattr(S9UR9BH_XD, "comment"):
    S9UR9BH_XD.comment()
elif hasattr(S9UR9BH_XD, "main"):
    S9UR9BH_XD.main()
else:
    print("⚠️ Module load ho gaya, lekin koi entry function nahi mili")
    print("Available:", dir(S9UR9BH_XD))
