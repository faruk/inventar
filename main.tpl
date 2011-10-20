<html>
<head>

<style type = "text/css">
#menu {
  width:200px;
  background-color:black;
  color:white;
  float:left;
}

#menu a, a.visited {
  text-decoration:none;
  color:white;
}

#menu a.hover {
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
    <li><a href="/software">software</a></li>
    <li><a href="/room">room</a></li>
    <li><a href="/user">user</a></li>
    <li><a href="/departement">department</a></li>
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

</body>
</html>
