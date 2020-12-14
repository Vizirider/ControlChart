import dash
import dash_html_components as html

def test_bsly000_falsy_child(dash_br):

    dash_br.server_url = 'http://127.0.0.1:8050/'

    assert dash_br.wait_for_element("label").text == "Összes mintavétel"
    assert dash_br.get_logs() == [], "browser should contain no error"

    dash_br.percy_snapshot("dash testing page")


def test_bsly001_falsy_child(dash_duo):

    app = dash.Dash(__name__)
    app.layout = html.Div(id='upload-data', children=0)

    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal('upload-data', "0", timeout=2)

    assert dash_duo.find_element('upload-data').text == "0"

    assert dash_duo.get_logs() == [], "browser console should contain no error"

    dash_duo.percy_snapshot("bsly001-layout")
    
