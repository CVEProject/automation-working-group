#!/usr/bin/env python
import sys
import argparse

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        json = None

try:
    import jsonschema
    import jsonschema.exceptions

except ImportError:
    jsonschema = None


def jsonvalidation(json_doc_paths, json_schema_path):
    with open(json_schema_path, 'r') as fp:
        schema_doc = json.load(fp)

    for json_doc_path in json_doc_paths:
        try:
            with open(json_doc_path, 'r') as fp:
                json_doc = json.load(fp)

            jsonschema.validate(json_doc, schema_doc)
            sys.stdout.write("Record `%s` passed validation\n" % json_doc_path)

        except jsonschema.exceptions.ValidationError as incorrect:
            v = jsonschema.Draft4Validator(schema_doc)

            errors = sorted(v.iter_errors(json_doc), key=lambda e: e.path)
            for error in errors:
                sys.stderr.write("Record `%s` did not pass:\n" % json_doc_path)
                sys.stderr.write(str(error.message) + "\n")

        except Exception as ex:
            sys.stderr.write("Record `%s` did not pass: %s\n" % (json_doc_path, ex))


def main():
    parser = argparse.ArgumentParser(
        description = "Validate one of more JSON files against JSON schema"
    )

    parser.add_argument('schema', type=str,
                        help='Path to JSON schema file to use')
    parser.add_argument('jsondoc', type=str, nargs='+',
                        help='Path to JSON file(s) to verify against given JSON schema')

    args = parser.parse_args()

    if not json:
        sys.stderr.write("Please install the `simplejson` package\n")
        sys.exit(1)

    if not jsonschema:
        sys.stderr.write("Please install the `jsonschema` package\n")
        sys.exit(1)

    jsonvalidation(args.jsondoc, args.schema)


if __name__ == '__main__':
    main()
