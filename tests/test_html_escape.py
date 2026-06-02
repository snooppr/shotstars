"""Regression tests for HTML escaping of untrusted GitHub-API data in the report.

A repository `description` is fully controlled by the repository owner. Before the
fix it was written verbatim into the generated `report.html`, which Shotstars then
auto-opens in the user's browser via `webbrowser.open("file://.../report.html")`.
A crafted description such as `<img src=x onerror=...>` therefore executed
JavaScript in the local `file://` origin.

These tests pin the escaping helper used at the report sink so the injection
vectors stay neutralized.
"""

import os
import unittest

# shotstars.shotstars selects an ASCII banner at import time using
# os.get_terminal_size(), which raises OSError when stdout is not a TTY
# (e.g. under a test runner). Provide a stable size so the import succeeds.
os.get_terminal_size = lambda *a, **k: os.terminal_size((120, 40))

from shotstars.shotstars import escape_html


class TestEscapeHtml(unittest.TestCase):
    def test_script_tag_is_neutralized(self):
        payload = "<script>alert(1)</script>"
        out = escape_html(payload)
        self.assertNotIn("<script>", out)
        self.assertIn("&lt;script&gt;", out)

    def test_event_handler_attribute_breakout_is_neutralized(self):
        payload = '"><img src=x onerror=alert(1)>'
        out = escape_html(payload)
        self.assertNotIn("<img", out)
        self.assertNotIn('"', out)  # quote=True closes attribute-context breakout

    def test_plain_text_is_preserved(self):
        text = "A normal repository description (v1.0)."
        self.assertEqual(escape_html(text), text)

    def test_non_string_input_is_coerced(self):
        self.assertEqual(escape_html(123), "123")


if __name__ == "__main__":
    unittest.main()
