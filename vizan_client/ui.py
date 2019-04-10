from __future__ import absolute_import
import json
import requests
import tempfile
from .json_utils import CobraSolutionEncoder
from io import open


def visualise(model_filename, svg_filename, output_filename, analysis_type='FBA',
              analysis_results=None, url=None):
    if analysis_type is None:
        analysis_type = 'FBA'
    if analysis_results is not None:
        if analysis_type == 'FBA':
            results_json = json.dumps(analysis_results, cls=CobraSolutionEncoder)
        if analysis_type == 'FVA':
            results_json = analysis_results.to_json()
        results_file = tempfile.SpooledTemporaryFile(max_size=10*1024*1024)
        results_file.write(results_json.encode("utf-8"))
        results_file.seek(0)
    else:
        results_file = None
    files = {
        'model': open(model_filename, 'rb'),
        'svg': open(svg_filename, 'rb'),
        'analysis_results': results_file,
    }
    values = {'analysis_type': analysis_type}
    if url is None:
        url = "https://localhost/2/"
        verify = False
    else:
        verify = True

    svg_content = make_http_request(url, files, values, verify=verify)
    with open(output_filename, 'wb') as f:
        f.write(svg_content)


def make_http_request(url, files, data, verify=True):
    r = requests.post(url, files=files, data=data, verify=verify)
    print(r.status_code, r.reason)
    if r.status_code == 200:
        res = r.content
    else:
        raise Exception("Status code is not 200, but {}".format(r.status_code))
    return res
