# Foundations Resources

> Curated from `catalog.yaml`. Pilot coverage reviewed on 2026-09-15.

## `php-supported-versions` — PHP Supported Versions
- **URL:** https://www.php.net/supported-versions.php
- **Topics:** php-runtime, php-versioning
- **Depth:** `core`
- **Version scope:** PHP support lifecycle; currently 8.2–8.5 supported
- **Use:** Use to choose a supported runtime; do not make the curriculum depend on one point release.

## `php-types-manual` — PHP Manual — Types
- **URL:** https://www.php.net/manual/en/language.types.php
- **Topics:** php-type-system, php-type-coercion
- **Depth:** `core`
- **Version scope:** current PHP manual
- **Use:** Primary source for Week 1 type-system experiments.

## `php-oop-manual` — PHP Manual — Classes and Objects
- **URL:** https://www.php.net/manual/en/language.oop5.php
- **Topics:** php-oop, interfaces, abstract-final, inheritance
- **Depth:** `core`
- **Version scope:** current PHP manual
- **Use:** Primary Week 2 language reference; use design experiments to teach trade-offs, not syntax memorization.

## `php-errors-exceptions` — PHP Manual — Errors and Exceptions
- **URL:** https://www.php.net/exceptions
- **Topics:** php-errors, php-exceptions, throwable, debugging
- **Depth:** `core`
- **Version scope:** current PHP manual
- **Use:** Primary Week 4 failure-model reference; pair with prediction and reproducible failure experiments.

## `composer-basic-usage` — Composer — Basic Usage
- **URL:** https://getcomposer.org/doc/01-basic-usage.md
- **Topics:** composer, composer-autoload
- **Depth:** `core`
- **Version scope:** current Composer documentation
- **Use:** Use with hands-on dependency/autoload experiments.

## `composer-schema` — Composer — composer.json Schema
- **URL:** https://getcomposer.org/doc/04-schema.md
- **Topics:** composer, psr4, dependency-management
- **Depth:** `core`
- **Version scope:** current Composer documentation
- **Use:** Reference for autoload/version/config details.

## `git-pro-book` — Pro Git
- **URL:** https://git-scm.com/book/en/v2
- **Topics:** git, git-branching, git-recovery
- **Depth:** `core`
- **Version scope:** Git concepts; living online edition
- **Use:** Primary Git conceptual reference.

## `cakephp-5-orm` — CakePHP 5 — Database Access & ORM
- **URL:** https://book.cakephp.org/5.x/orm.html
- **Topics:** cakephp, orm, legacy-modernization
- **Depth:** `core`
- **Version scope:** CakePHP 5.x
- **Use:** Use to contrast ORM behavior with underlying SQL.

## `cakephp-5-testing` — CakePHP 5 — Testing
- **URL:** https://book.cakephp.org/5.x/development/testing.html
- **Topics:** cakephp, testing, legacy-modernization
- **Depth:** `core`
- **Version scope:** CakePHP 5.x
- **Use:** Primary source for characterization/integration tests in Project A.

## `phpunit-writing-tests` — PHPUnit 12.5 Manual — Writing Tests
- **URL:** https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html
- **Topics:** phpunit, unit-testing, assertions, exception-testing
- **Depth:** `core`
- **Version scope:** PHPUnit 12.5; use a runtime-compatible major when project PHP differs
- **Use:** Primary Week 3 testing reference; concepts are stable while the project should pin a compatible major.

## `phpstan-getting-started` — PHPStan — Getting Started
- **URL:** https://phpstan.org/user-guide/getting-started
- **Topics:** static-analysis, phpstan
- **Depth:** `core`
- **Version scope:** current PHPStan docs
- **Use:** Use for a measurable static-analysis baseline.

## `xdebug-step-debugging` — Xdebug — Step Debugging
- **URL:** https://xdebug.org/docs/step_debug
- **Topics:** xdebug, debugging, breakpoints, php
- **Depth:** `supporting`
- **Version scope:** current Xdebug documentation
- **Use:** Week 4 supporting-platform reference; form a hypothesis before stepping through code.
