<html>
<head>
<script type="text/javascript" src="/js/jquery-1.6.4.min.js"></script>
<script type="text/javascript" src="/js/ui/jquery-ui-1.8.16.custom.js"></script>
<script type="text/javascript" src="/js/ui/jquery.ui.widget.js"></script>
<script type="text/javascript" src="/js/ui/jquery.ui.datepicker.js"></script>
<link type="text/css" href="/js/css/smoothness/jquery-ui-1.8.16.custom.css" rel="Stylesheet" />


<style type = "text/css">
#menu {
  
  top:20px;
  margin-right: 20px;
  width:200px;
  background-color:black;
  color:white;
  float:left;
  z-index:1;
}

#menu ul li a, a.visited {
  text-decoration:none;
  color:white;
}

#menu ul li a.hover {
  background-color:white;
  color:black;
}

#content {
}

</style>


</head>
<body>

<div id="menu">
  <ul>
    <li><a href="/hardware">hardware</a></li>
    <ul>
      <li><a href="/hardware/new">new</a></li>
    </ul>
    <li><a href="/software">software</a></li>
    <ul>
      <li><a href="/software/new">new</a></li>
    </ul>
    <li><a href="/room">room</a></li>
    <ul>
      <li><a href="/room/new">new</a></li>
    </ul>
    <li><a href="/user">user</a></li>
    <ul>
      <li><a href="/user/new">new</a></li>
    </ul>
    <li><a href="/department">department</a></li>
    <ul>
      <li><a href="/department/new">new</a></li>
    </ul>
  </ul>
</div>

<div id="content">
  %if content:
    <h1>Welcome To Jan's Inventory System</h1>
    <p>
      {{content}}
    </p>
  %else:
    %include
  %end
</div>

<script type="text/javascript">
  //$(function() {
  //  $( "#datepicker" ).datepicker();
  //});

  $(document).ready(function() {
    $(function() {
      $( "#datepicker" ).datepicker();
    });
  });

</script>

</body>
</html>
