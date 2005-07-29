import locationreport
import scenereport
import u

# tests location report (just that it runs without exceptions, for now)

def testBasic():
    sp = u.load()
    report = locationreport.LocationReport(scenereport.SceneReport(sp))
    data = report.generate(False)

    # try to catch cases where generate returns something other than a PDF
    # document
    assert len(data) > 200
    assert data[:8] == "%PDF-1.4"
