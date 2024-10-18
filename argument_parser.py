import argparse


def python_Arg():
    parser = argparse.ArgumentParser("S3 bucket interactions")
    parser.add_argument(
        "-l",
        "--list",
        help="list all files in the TIE-rp directory",
        dest="list",
        action="store_true",
    )
    parser.add_argument(
        "-u",
        "--upload",
        nargs=2,
        metavar=("filename", "destination"),
        help="upload file to a specific directory",
        dest="upload",
    )
    parser.add_argument(
        "-f", "--filter", type=str, help="list files matiching filter", dest="filter"
    )
    parser.add_argument(
        "-d", "--delete", type=str, help="delete files matching filter", dest="delete"
    )

    return parser.parse_args()
