import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def run(script, *args):
    # Run through python3, not by executing the script directly: the
    # scripts have no .py extension and lose their executable bit on
    # GitHub, so a fresh clone cannot run them directly.
    result = subprocess.run(
        [sys.executable, str(HERE / script), *args],
        capture_output=True, timeout=30,
    )
    assert result.returncode == 0, result.stderr.decode()
    return result


class TestVigenere(unittest.TestCase):
    def test_keygen_makes_key_of_requested_length(self):
        with tempfile.TemporaryDirectory() as tmp:
            key = Path(tmp) / "key.bin"
            run("keygen", "16", str(key))
            self.assertEqual(len(key.read_bytes()), 16)

    def test_encrypt_decrypt_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            key = Path(tmp) / "key.bin"
            plain = Path(tmp) / "plain.txt"
            cipher = Path(tmp) / "cipher.bin"
            back = Path(tmp) / "back.txt"
            plain.write_bytes(b"hello world, this is a test")
            run("keygen", "8", str(key))
            with open(cipher, "wb") as out:
                subprocess.run(
                    [sys.executable, str(HERE / "encrypt"), str(plain), str(key)],
                    stdout=out, check=True, timeout=30,
                )
            with open(back, "wb") as out:
                subprocess.run(
                    [sys.executable, str(HERE / "decrypt"), str(cipher), str(key)],
                    stdout=out, check=True, timeout=30,
                )
            self.assertEqual(back.read_bytes(), plain.read_bytes())

    def test_two_keys_are_different(self):
        with tempfile.TemporaryDirectory() as tmp:
            k1 = Path(tmp) / "k1.bin"
            k2 = Path(tmp) / "k2.bin"
            run("keygen", "16", str(k1))
            run("keygen", "16", str(k2))
            self.assertNotEqual(k1.read_bytes(), k2.read_bytes())


if __name__ == "__main__":
    unittest.main()
