#!/usr/bin/env python3

import argparse
import os
import subprocess

import _hkml

def set_argparser(parser):
    _hkml.set_manifest_mlist_options(parser, mlist_nargs='*')
    parser.add_argument('--quiet', '-q', default=False, action='store_true',
            help='Work silently.')

def fetch_mail(manifest_file, mail_lists, quiet=False):
    manifest = _hkml.get_manifest(manifest_file)
    if not manifest:
        print("Cannot open manifest file %s" % manifest_file)
        parser.print_help()
        exit(1)

    site = manifest['site']
    for mlist in mail_lists:
        repo_paths = _hkml.mail_list_repo_paths(mlist, manifest)
        local_paths = _hkml.mail_list_data_paths(mlist, manifest)
        for idx, repo_path in enumerate(repo_paths):
            git_url = '%s%s' % (site, repo_path)
            local_path = local_paths[idx]
            if not os.path.isdir(local_path):
                cmd = 'git clone --mirror %s %s' % (git_url, local_path)
            else:
                cmd = 'git --git-dir=%s remote update' % local_path
            if not quiet:
                print(cmd)
                subprocess.call(cmd.split())
            else:
                with open(os.devnull, 'w') as f:
                    subprocess.call(cmd.split(), stdout=f)

def main(args=None):
    if not args:
        parser = argparse.ArgumentParser()
        set_argparser(parser)
        args = parser.parse_args()

    manifest_file = args.manifest
    if not manifest_file:
        manifest_file = os.path.join(_hkml.get_hkml_dir(), 'manifest')
    mail_lists = args.mlist
    if not mail_lists:
        mail_lists = _hkml.fetched_mail_lists()
    quiet = args.quiet
    fetch_mail(manifest_file, mail_lists, quiet)

if __name__ == '__main__':
    main()
