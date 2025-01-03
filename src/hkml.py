#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0

import argparse
import os
import subprocess
import sys

import hkml_init
import hkml_interactive
import hkml_fetch
import hkml_list
import hkml_thread
import hkml_open
import hkml_reply
import hkml_forward
import hkml_tag
import hkml_send
import hkml_write
import hkml_sync
import hkml_export
import hkml_monitor
import hkml_patch
import hkml_manifest
import hkml_cache
import hkml_signature

import _hkml

class SubCmdHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _format_action(self, action):
        parts = super(argparse.RawDescriptionHelpFormatter,
                self)._format_action(action)
        # Skips subparsers help
        if action.nargs == argparse.PARSER:
            parts = '\n'.join(parts.split('\n')[1:])
        return parts

parser = argparse.ArgumentParser(formatter_class=SubCmdHelpFormatter)
parser.add_argument('--hkml_dir', metavar='hkml dir', type=str)
parser.add_argument('-C', '--directory', metavar='<dir>',
                    help='change to <dir> before doing anything')

subparsers = parser.add_subparsers(title='command', dest='command',
        metavar='<command>')
# subparsers.default = 'interactive'

parser_init = subparsers.add_parser('init', help = 'initialize working dir')
hkml_init.set_argparser(parser_init)

parser_fetch = subparsers.add_parser('fetch', help = 'fetch mails')
hkml_fetch.set_argparser(parser_fetch)

parser_list = subparsers.add_parser('list', help = 'list mails')
hkml_list.set_argparser(parser_list)

parser_thread = subparsers.add_parser(
        'thread', help = 'list mails of a thread')
hkml_thread.set_argparser(parser_thread)

parser_open = subparsers.add_parser('open', help = 'open a mail')
hkml_open.set_argparser(parser_open)

parser_reply = subparsers.add_parser('reply', help = 'reply to a mail')
hkml_reply.set_argparser(parser_reply)

parser_forward = subparsers.add_parser('forward', help = 'forward a mail')
hkml_forward.set_argparser(parser_forward)

parser_tag = subparsers.add_parser('tag', help = 'manage tags of mails')
hkml_tag.set_argparser(parser_tag)

parser_fmtml = subparsers.add_parser('write', help = 'write a mail')
hkml_write.set_argparser(parser_fmtml)

parser_send = subparsers.add_parser('send', help = 'send mails')
hkml_send.set_argparser(parser_send)

parser_sync = subparsers.add_parser('sync',
                                    help = 'synchronize setups and outputs')
hkml_sync.set_argparser(parser_sync)

parser_export = subparsers.add_parser('export', help = 'export mails')
hkml_export.set_argparser(parser_export)

parser_monitor = subparsers.add_parser('monitor', help = 'monitor mails')
hkml_monitor.set_argparser(parser_monitor)

parser_patch = subparsers.add_parser('patch', help = 'apply mail as patch')
hkml_patch.set_argparser(parser_patch)

parser_manifest = subparsers.add_parser('manifest', help = 'print manifest')
hkml_manifest.set_argparser(parser_manifest)

parser_cache = subparsers.add_parser('cache', help = 'manage cache')
hkml_cache.set_argparser(parser_cache)

parser_signatures = subparsers.add_parser(
        'signature', help = 'manage signatures')
hkml_signature.set_argparser(parser_signatures)

args = parser.parse_args()

if args.directory is not None:
    os.chdir(args.directory)

if not args.command == 'init':
    manifest = None
    if hasattr(args, 'manifest'):
        manifest = args.manifest
    _hkml.set_hkml_dir_manifest(args.hkml_dir, manifest)

if not args.command:
    parser.print_help()
    exit(1)

if args.command == 'init':
    hkml_init.main(args)
elif args.command == 'list':
    hkml_list.main(args)
elif args.command == 'thread':
    hkml_thread.main(args)
elif args.command == 'fetch':
    hkml_fetch.main(args)
elif args.command == 'open':
    hkml_open.main(args)
elif args.command == 'reply':
    hkml_reply.main(args)
elif args.command == 'forward':
    hkml_forward.main(args)
elif args.command == 'tag':
    hkml_tag.main(args)
elif args.command == 'write':
    hkml_write.main(args)
elif args.command == 'sync':
    hkml_sync.main(args)
elif args.command == 'send':
    hkml_send.main(args)
elif args.command == 'export':
    hkml_export.main(args)
elif args.command == 'monitor':
    hkml_monitor.main(args)
elif args.command == 'patch':
    hkml_patch.main(args)
elif args.command == 'manifest':
    hkml_manifest.main(args)
elif args.command == 'cache':
    hkml_cache.main(args)
elif args.command == 'signature':
    hkml_signature.main(args)
# elif args.command == 'interactive':
#     hkml_interactive.main(args)
else:
    print('wrong command (%s)' % args.command)
    exit(1)
