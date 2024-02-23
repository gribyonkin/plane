#from fileinput import filename
from ru.travelfood.simple_ui import SimpleUtilites as suClass
import base64


def template_html_plane(hashMap,_files=None,_data=None):
    
    from io import BytesIO
   
    filename = suClass.get_stored_file("template1")
    hashMap.put("toast", filename)
    with open(filename) as file1_:
        htmltxt = file1_.read()

    planename = suClass.get_stored_file("plane")
    hashMap.put("toast", planename)
    #with open(planename,"rb") as file2_:
    #    encoded_string = base64.b64encode(file2_.read())
    #    planetxt = file2_.read()
    #htmltxt.replace("###",planetxt)

    #htmltxt.replace("&nbsp"," ")
    hashMap.put("html_plane_all", htmltxt)

    return hashMap

def html_plane_open(hashMap,_files=None,_data=None):
    
    hashMap.remove("html_plane_all")
    #https://cdnjs.cloudflare.com/ajax/libs/raphael/2.2.0/raphael-min.js
    #

    filename = suClass.get_stored_file("plane")
    hashMap.put("toast", filename)
    htmlstring = """
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>    
        <script src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.2.0/raphael-min.js"></script>
        <meta content="text/html;charset=UTF-8" http-equiv="Content-Type" />
        <meta content="UTF-8" http-equiv="encoding" />
        <meta http-equiv="pragma" content="no-cache" />
        <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE8" />
        <script type="text/javascript">
        var boxListing = [
        {x : '100', y : '0', width : '100', height : '100', status : 'FREE', boxname : 'Box 1', GUID : 'id-001-111'}, 
        {x : '0', y : '100', width : '100', height : '100', status : 'BUSY', boxname : 'Box 2', GUID : 'id-002-222'}, 
        {x : '200', y : '100', width : '100', height : '100', status : 'FREE', boxname : 'Box 3', GUID : 'id-003-333'}, 
        {x : '0', y : '200', width : '100', height : '100', status : 'OFFICE', boxname : 'Box 4', GUID : 'id-004-444'}
        ];
        var raphObject; 
        var radiusRect = 5;
        function startup() {
            raphObject = Raphael('canvasdiv', 300, 300);
            drawBoxes();
        }
        function drawBoxes() {
            boxList = new Array();
            boxListText = new Array();
            boxListDrag = new Array();
            var c = raphObject.image(" """+filename+ """", 0, 0, 300, 300);
            for(var i = 0; i < boxListing.length; i++) {
                var px = boxListing[i].x;
                var py = boxListing[i].y;
                var pw = boxListing[i].width;
                var ph = boxListing[i].height;
                var uid = boxListing[i].GUID;
                var status = boxListing[i].status;
                var textx = 0;
                var texty = 0;               
                px = parseInt(px);
                py = parseInt(py);
                pw = parseInt(pw);
                ph = parseInt(ph);                
                textx = px + (pw * 20/100);
                texty = py + (ph * 10/100);
                colorBoxFree = '#2AAC55';
                colorBoxBusy = '#ABA529';
                colorBoxOffice = '#C2C8FC';
                if (status == 'FREE') {colorBox = colorBoxFree};
                if (status == 'BUSY') {colorBox = colorBoxBusy};
                if (status == 'OFFICE') {colorBox = colorBoxOffice};
                boxList[i] = raphObject.rect(px, py, pw, ph, radiusRect)
                    .attr('fill', colorBox)
                    .attr('opacity', 0.9)
                    .data('uid', uid)
                    .data('status', status)
                    .click(function()
                        {
                            callJS(this.data("uid"));
                        }
                        )
                ;            
                boxListText[i] = raphObject.text(textx, texty, boxListing[i].boxname)
                    .attr('font', '12px Arial')
                    .attr('fill', '#000000');                            
            } //for loop
        }
        </script>
    </head>
    <body onload="startup();">
    <div id="canvasdiv" style="width: 300px; height: 300px;"></div>
    <script type="text/javascript">
        function callJS(param) {
            Android.onInput(param);
        }
    </script>
    </body>
    </html>    
    """

    #htmlstring.replace("~~~",suClass.get_stored_file("raphael.min"))
    #htmlstring.replace("&nbsp"," ")
    if not hashMap.containsKey("html_plane_all"):
        hashMap.put("html_plane_all",htmlstring)
        #hashMap.put("RefreshScreen","Общий план")
    
    #hashMap.put("html_plane_all",htmlstring)    

    return hashMap 

def html_plane_input(hashMap,_files=None,_data=None):
    
    hashMap.put("ref_corp", hashMap.get("jsdata"))

    hashMap.put("toast", hashMap.get("ref_corp"))
    hashMap.put("ref_flow", hashMap.get("ref_corp"))
    hashMap.put("RefreshScreen","Общий план")
    #hashMap.put("html_plane_all", "")
    #hashMap.put("ShowScreen", "Corpus")
    
    return hashMap

def finish_process_plane(hashMap,_files=None,_data=None):
    hashMap.remove("html_plane_all")
    hashMap.put("FinishProcess", "ПЛАН")

    return hashMap

def html_close_corp(hashMap,_files=None,_data=None):
        
    #if hashMap.get("listener")=="btn_close_floors":
    hashMap.put("ShowScreen", "Общий план")

    return hashMap

#hashMap.put("toast",hashMap.get("listener"))

def show_listener(hashMap,_files=None,_data=None):

    #hashMap.put("RefreshScreen","Общий план")
    hashMap.put("ShowScreen", "Corpus")
    #hashMap.put("toast",hashMap.get("listener"))

    return hashMap

def show_plane(hashMap,_files=None,_data=None):

    hashMap.put("ShowScreen", "Corpus")

    return hashMap