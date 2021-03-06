# coding=utf-8
"""
© 2013 LinkedIn Corp. All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at  http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
"""
import os
import random

def graph_csv(output_directory, csv_file, plot_title, output_filename, y_label=None, precision=None, graph_height="600", graph_width="1500"):
  """ Single metric graphing function """
  if not os.path.getsize(csv_file):
    return False, ""
  y_label = y_label or plot_title
  div_id = str(random.random())
  div_string = "<div id=\"%s\" style=\"width:%spx; height:%spx;\"></div>" % (div_id, graph_width, graph_height)
  script_string = """<script type=\"text/javascript\">
        g2 = new Dygraph(
          document.getElementById(\"""" + div_id + """"),
            \"""" + os.path.basename(csv_file) +  """",
            {
                     axes: {
                        x: {
                            valueFormatter: Dygraph.dateString_,
                            valueParser: function(x) { return Date.parseHttpTimeFormat(x); },
                            ticker: Dygraph.dateTicker
                        }
                     },
                        xlabel: "Time",
                        ylabel: \"""" + y_label + """",
                        title: \"""" + plot_title + """",
                        labels: ["Time",\"""" + y_label + """"]
            }          // options
        );
        </script>"""

  #Ritesh: TODO Also generate PNGs if someone needs them separately
  return True, div_string + script_string

