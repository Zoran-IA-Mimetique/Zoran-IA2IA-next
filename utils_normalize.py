from typing import Any, Dict, List
import json, csv, io
from xml.etree import ElementTree as ET

def _xml_to_dict(elem):
    d = {elem.tag: {} if elem.attrib else None}
    children = list(elem)
    if children:
        dd = {}
        for dc in map(_xml_to_dict, children):
            for k, v in dc.items():
                if k in dd:
                    if not isinstance(dd[k], list):
                        dd[k] = [dd[k]]
                    dd[k].append(v)
                else:
                    dd[k] = v
        d = {elem.tag: dd}
    if elem.attrib:
        d[elem.tag].update(('@' + k, v) for k, v in elem.attrib.items())
    if elem.text:
        text = elem.text.strip()
        if children or elem.attrib:
            if text:
                d[elem.tag]['#text'] = text
        else:
            d[elem.tag] = text
    return d

def fast_normalize(raw: Any):
    """Best-effort normalizer for JSON/CSV/XML/string."""
    # Already dict
    if isinstance(raw, dict):
        return raw
    # JSON string
    if isinstance(raw, str):
        s = raw.strip()
        # JSON
        if s.startswith('{') or s.startswith('['):
            return json.loads(s)
        # CSV (simple)
        if ',' in s and '\n' in s and not s.lstrip().startswith('<'):
            buf = io.StringIO(s)
            reader = csv.DictReader(buf)
            return {"rows": list(reader)}
        # XML
        if s.lstrip().startswith('<'):
            root = ET.fromstring(s)
            return _xml_to_dict(root)
        # Fallback as plain text
        return {"text": s}
    # Bytes
    if isinstance(raw, (bytes, bytearray)):
        try:
            return fast_normalize(raw.decode('utf-8'))
        except Exception:
            return {"bytes": list(raw)}
    # List/tuple → wrap
    if isinstance(raw, (list, tuple)):
        return {"items": list(raw)}
    # Unknown
    return {"value": str(raw)}
