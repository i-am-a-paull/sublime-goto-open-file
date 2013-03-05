##GotoOpenFile

Sometimes, if you are working on a small subsection of a particularly large
project, Goto Anything might get too distracting. GotoOpenFile brings up a quick
panel that only includes currently-opened tabs.

For tabs in the active group, the default keybinding is ctrl-shift-o (or
cmd-shift-o).

For tabs in the entire window, the default keybinding is alt-shift-o.

By default, tabs are not sorted by name. However, if you would like them to be,
you can set "sort_views" to true.

In your user settings:

```JSON

"GotoOpenFile": {
  "sort_views": true
}

```


This plugin is licensed under the 2-clause BSD license:

```
Copyright (c) 2012-2013, project authors (https://github.com/phildopus/sublime-goto-open-file/CONTRIBUTORS.md)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

```
