<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title></title>
 <link href="images/a.css" rel="stylesheet" type="text/css">
<style>
.trans_box{
    width: 400px;
	height:300px;
    margin: 20px;
    overflow: hidden;
    bottom: 10px;
    left: 50%;
    margin-left: -200px;
    position: absolute;
    z-index:-100;
}
.trans_image_box {
    width: 1600px; 
    height: 300px;
    -webkit-transition: all 1s ease-in-out;
    -moz-transition: all 1s ease-in-out;
    -o-transition: all 1s ease-in-out;
    transition: all 1s ease-in-out;
}
.trans_image {
    width: 400px;
	height:300px;
    float: left;
}
</style>

<style>
.getp{
 position:relative;
 bottom:5px
}
</style>

</head>
 <style type="text/css">
html{
       height: 100%;
}
body{
       background-image:url(images/bgr.gif);
       background-size:100% 100%;
       padding: 0;
       margin: 0;
}
</style>

<body>
<div class="header"><strong><font size=10>鸟类识别</font></strong></div>
<div class="header"><strong><font size=10><jsp:include flush="fasle"
					page="getposition.html" /></font></strong></div>
					
<div class="getp"><jsp:include flush="fasle" page="uploadpic.jsp" /></div>
<table width="900" border="0" align="center" bottom="100px" cellpadding="0"
		cellspacing="0">
		<tr>
			<td height="50"></td>

		</tr>

		<tr>
			<td align="center" valign="top" height="400">

<script type="text/javascript" charset="utf-8"  src="https://files.cnblogs.com/files/liuzhou1/L2Dwidget.0.min.js"></script>
<script type="text/javascript" charset="utf-8"  src="https://files.cnblogs.com/files/liuzhou1/L2Dwidget.min.js"></script>
<script src="https://eqcn.ajz.miesnfu.com/wp-content/plugins/wp-3d-pony/live2dw/lib/L2Dwidget.min.js"></script>
<script>
    L2Dwidget.init({      
      "model": {  
            jsonPath: "https://unpkg.com/live2d-widget-model-tsumiki/assets/tsumiki.model.json",        
           "scale": 1
        },     
          "display": {      
            "position": "right", 
            "width": 150,  
            "height": 300, 
            "hOffset": 0,     
            "vOffset": -20
        },       
           "mobile": {        
           "show": true,
           "scale": 0.5
        },
        "react": {
            "opacityDefault": 2,
            "opacityOnHover": 2        }
    });
</script>
<div class="trans_box">
    <div id="transImageBox" class="trans_image_box">
        <img class="trans_image" src="images/1.jpg" />
        <img class="trans_image" src="images/2.jpg" />
        <img class="trans_image" src="images/3.jpg" />
        <img class="trans_image" src="images/4.jpg" />
    </div>
</div>
<script language="javascript">
var int=self.setInterval("change()",2*1000);
var time=self.setInterval("clock()",3*1000);
var i=1;
function clock(){
	i=i+1;
	if(i==5){
		i=1;
	}
}
function change(){
	var a=document.getElementById("transImageBox");
	a.style.marginLeft=(1-i)*400+"px";
}
</script>
		</td>
		
		</tr>
</table>
</body>
</html>