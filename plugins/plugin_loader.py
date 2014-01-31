#!/usr/bin/python
# -*- coding: utf-8 -*-

import plugin_base
import os
import imp

#ordenar por un criterio (nombre)
def criterio(it1, it2):
    if not hasattr(it1, 'nombre') or not hasattr(it1, 'icon') or not hasattr(it1, 'run') or not \
       hasattr(it2, 'nombre') or not hasattr(it2, 'icon') or not hasattr(it2, 'run'):
           return 0
    obj1 = it1()
    obj2 = it2()

    return cmp(obj1.nombre(), obj2.nombre())


def cargar_plugins(pluginsdir = 'plugins'):
    for root, dirs, files in os.walk(pluginsdir):
        files = sorted(files)
        for fname in files:
            modname = os.path.splitext(fname)[0]
            try:
                module = imp.load_source(modname,os.path.join(root,fname))
            except Exception:
                continue

    # retornar la lista de plugins cargados ordenada por el nombre
    return sorted(plugin_base.plugins_list, cmp=criterio)
