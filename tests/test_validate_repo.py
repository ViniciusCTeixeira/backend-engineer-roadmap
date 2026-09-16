from pathlib import Path
import contextlib
import importlib.util
import io
import sys
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = PROJECT_ROOT / "scripts" / "validate_repo.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

spec = importlib.util.spec_from_file_location("roadmap_validator", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
sys.modules["roadmap_validator"] = validator
spec.loader.exec_module(validator)

class ValidatorContractTests(unittest.TestCase):
    def errors_for(self, fixture):
        return validator.validate_repository(FIXTURES / fixture)

    def assert_fixture_fails_with(self, fixture, code):
        errors = self.errors_for(fixture)
        self.assertTrue(errors, f"{fixture} unexpectedly passed")
        self.assertIn(code, {e.code for e in errors}, [e.render() for e in errors])

    def test_valid_fixture_passes(self):
        errors = self.errors_for("valid")
        self.assertEqual([], errors, [e.render() for e in errors])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = validator.main([str(FIXTURES / "valid")])
        self.assertEqual(0, rc)
        self.assertIn("Validation passed", out.getvalue())

    def test_duplicate_canonical_id_fails(self):
        self.assert_fixture_fails_with("duplicate-id", "DUPLICATE_ID")

    def test_invalid_study_mode_fails(self):
        self.assert_fixture_fails_with("invalid-mode", "INVALID_MODE")

    def test_missing_required_frontmatter_fails(self):
        self.assert_fixture_fails_with("missing-frontmatter", "MISSING_FRONTMATTER")

    def test_private_study_link_fails_but_prose_reference_is_allowed(self):
        self.assert_fixture_fails_with("leaked-study", "PRIVATE_LINK")

    def test_broken_internal_markdown_link_fails(self):
        self.assert_fixture_fails_with("broken-link", "BROKEN_LINK")

    def test_resource_without_last_verified_fails(self):
        self.assert_fixture_fails_with("invalid-resource", "RESOURCE_LAST_VERIFIED")

    def test_historical_assessment_template_requires_raw_attempt_feedback_split(self):
        self.assert_fixture_fails_with("invalid-history-template", "HISTORY_SEPARATION")

    def test_obsidian_local_state_must_not_be_public(self):
        self.assert_fixture_fails_with("obsidian-local-state", "OBSIDIAN_LOCAL_STATE")

    def test_missing_resource_reference_fails(self):
        self.assert_fixture_fails_with("missing-resource-ref", "UNKNOWN_RESOURCE_ID")

    def test_missing_week0_question_reference_fails(self):
        self.assert_fixture_fails_with("missing-question-ref", "UNKNOWN_QUESTION_ID")

    def test_tracked_private_study_file_fails(self):
        self.assert_fixture_fails_with("private-tracked", "PRIVATE_TRACKED")

    def test_invalid_technology_depth_fails(self):
        self.assert_fixture_fails_with("invalid-tech-depth", "INVALID_TECHNOLOGY_DEPTH")

    def test_public_answer_key_fails(self):
        self.assert_fixture_fails_with("public-answer-key", "PUBLIC_ANSWER_KEY")

    def test_public_solution_heading_fails(self):
        self.assert_fixture_fails_with("public-answer-heading", "PUBLIC_ANSWER_KEY")

    def test_resource_invalid_technology_depth_fails(self):
        self.assert_fixture_fails_with("invalid-resource-depth", "INVALID_TECHNOLOGY_DEPTH")

    def test_generated_python_cache_artifact_fails(self):
        self.assert_fixture_fails_with("generated-python-cache", "GENERATED_ARTIFACT")

    def test_inline_code_that_looks_like_wikilink_is_ignored(self):
        errors = self.errors_for("inline-code-link")
        self.assertEqual([], errors, [e.render() for e in errors])

if __name__ == "__main__":
    unittest.main()
