BLACK = "000000"
RED = "FF0000"
GREEN = "00FF00"
BLUE = "0000FF"
MAGENTA = "FF00FF"

SVG_START = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="{{PAPERWIDTH}}mm"
   height="{{PAPERHEIGHT}}mm"
   viewBox="0 0 {{PAPERWIDTH}} {{PAPERHEIGHT}}"
   version="1.1"
   id="{{ID}}"
   inkscape:version="1.0.2 (e86c870, 2021-01-15)"
   sodipodi:docname="{{FILENAME}}">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.5"
     inkscape:cx="236.8621"
     inkscape:cy="759.4905"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     inkscape:document-rotation="0"
     showgrid="false"
     inkscape:window-width="1267"
     inkscape:window-height="1040"
     inkscape:window-x="629"
     inkscape:window-y="0"
     inkscape:window-maximized="0" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
"""

SVG_END = "</svg>"

GROUP_START = """
  <g id="group_{{ID}}">
"""

GROUP_END = "</g>"

LAYER_START = """<g
     inkscape:label="{{NAME}}"
     inkscape:groupmode="layer"
     id="layer_{{ID}}">
"""

LAYER_END = "</g>"

PATH_XML = """
    <path
       id="{{ID}}"
       style="fill:none;fill-opacity:1;fill-rule:evenodd;stroke:#{{COLOR}};stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       fill="none" stroke="#{{COLOR}}"
       d="{{DATA}}"
       sodipodi:nodetypes="{{NODETYPES}}" />
"""

TEXT_XML = """
      <text xml:space="preserve"
         style="font-style:normal;font-weight:normal;font-size:6px;line-height:1;font-family:sans-serif;fill:#{{COLOR}};fill-opacity:1;stroke:none;stroke-width:0.1"
         x="{{X}}" y="{{Y}}"
         stroke="none" fill="#{{COLOR}}"
         id="{{ID}}"><tspan
           sodipodi:role="line"
           id="{{ID}}"
           x="{{X}}"
           y="{{Y}}"
           style="stroke-width:0.1">{{TEXT}}</tspan></text>
"""

ELLIPSE_XML = """
    <ellipse
       style="fill:none;fill-opacity:1;stroke:#{{COLOR}};stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none"
       fill="none" stroke="#{{COLOR}}"
       id="{{ID}}"
       cx="{{X}}"
       cy="{{Y}}"
       rx="{{R}}"
       ry="{{R}}" />
"""
