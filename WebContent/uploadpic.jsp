<%@page import="java.util.Date"%>
<%@page import="org.apache.commons.fileupload.FileItem"%>
<%@page import="java.util.List"%>
<%@page import="org.apache.commons.fileupload.servlet.ServletFileUpload"%>
<%@page import="org.apache.commons.fileupload.disk.DiskFileItemFactory"%>
<%@ page import="java.io.*"%>
<%@ page contentType="text/html;charset=UTF-8" language="Java"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>上传图片</title>
<style>
.container {
	position: absolute;
	top: 100px;
	left: 50%;
	text-align: center;
	width: 400px;
	margin-left: -200px;
}
</style>
</head>
<body>
	<%
		String imageUrl="";
		try {
			response.setContentType("text/html;charset=utf-8");
			request.setCharacterEncoding("utf-8");
			
			PrintWriter writer = response.getWriter();
			DiskFileItemFactory factory = new DiskFileItemFactory();
			File f = new File("E:\\SE");
			if (!f.exists()) {
				f.mkdirs();
			}
			factory.setRepository(f);
			ServletFileUpload fileupload = new ServletFileUpload(factory);
			fileupload.setHeaderEncoding("utf-8");
			
			if(request.getContentType()!=null){
				List<FileItem> fileitems = fileupload.parseRequest(request);
				for (FileItem fileitem : fileitems) {
					if (fileitem.isFormField()) {
// 						writer.print(fileitem.getFieldName()+"：" + fileitem.getString("utf-8") + "<br>");
					} else {
					
						String filename = fileitem.getName();
// 						System.out.println(filename);
						if (filename != null && !filename.equals("")) {
							String prefix 	= 	filename.substring(0,filename.lastIndexOf("."));
							String suffix	=	filename.substring(filename.lastIndexOf("."));
							filename=prefix+"_"+new Date().getTime()+suffix;
							String webPath = "/upload/";
// 							System.out.println(request.getContextPath());
							String filepath = getServletContext().getRealPath(webPath);
							File webFile = new File(filepath);
							if (!webFile.exists()) {
								webFile.mkdirs();
							}

//	 						System.out.println("服务器目录路径：" + filepath);
							filepath=filepath+filename;
//	 						System.out.println("服务器文件路径：" + filepath);
							File file = new File(filepath);
							if (!file.exists()) {
								file.createNewFile();
							}

							InputStream in = fileitem.getInputStream();

							String path = "D://Code//SE作业//WebContent";
							String uploadName=path+"/upload/";
							File upload=new File(uploadName);
							if (!upload.exists()) {
								upload.mkdirs();
							}
							FileOutputStream out1 = new FileOutputStream(file);
							FileOutputStream out2 = new FileOutputStream(uploadName+filename);
							byte[] buffer = new byte[1024];
							int len;
							while ((len = in.read(buffer)) > 0){
								out1.write(buffer, 0, len);
								out2.write(buffer, 0, len);
							}
							in.close();
							out1.close();
							out2.close();

							fileitem.delete();
							f.delete();
							imageUrl=request.getContextPath()+webPath+filename;
// 							System.out.println("图片路径"+imageUrl);
						}
					}
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("出错了");
		}
	%>
	<div class="container">
		<form action="uploadpic.jsp" enctype="multipart/form-data" method="post"
			>
			<table>
				<tr>
					<td>
						<img src="<%=imageUrl%>" alt="图片为空" id="image" width="400px" height="225px" align="middle">
					</td>
				</tr>
				<tr>
					<td>
						<input type="file" name="File" id="File" onchange="changeFile()" required="true">
					</td>
					
				</tr>
				<tr>
					<td>
						<button type="submit">上传</button>
					</td>
				</tr>
			</table>
		</form>
	</div>
	<script type="text/javascript">
		function changeFile() {
			var image = document.getElementById('image');
			var name = document.getElementById('File').files[0];
			var url;
			if (name) {
				url = window.URL.createObjectURL(name);
			}
			image.src = url;
		}
		
	</script>



</body>
</html>

