<html>
<head>
    <link rel="stylesheet" href="/css/bootstrap/css/bootstrap.css" type="text/css">
</head>
<body>
    <div class="navbar">
        <div class="navbar-inner">
            <div class="container">
                <ul class="nav">
                    <a class="brand" href="/">OEI INVENTAR</a>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            hardware
                        <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <a href="/hardware/all">all</a>
                            </li>
                            <li>
                                <a href="/hardware/new">new</a>
                            </li>
                            <li>
                                <a href="/software/install">install software</a>
                            </li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            software
                        <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <a href="/software/all">all</a>
                            </li>
                            <li>
                                <a href="/software/new">new</a>
                            </li>
                            <li>
                                <a href="/hardware/install">install software</a>
                            </li>
                        </ul>
                    </li>
                    <li><a href="/installations">installations</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            rooms 
                        <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <a href="/room/all">all</a>
                            </li>
                            <li>
                                <a href="/room/new">new</a>
                            </li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            department
                        <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <a href="/department/all">all</a>
                            </li>
                            <li>
                                <a href="/department/new">new</a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container">
        %include
    </div>

    <script src="/js/jquery.js"></script>
    <script src="/css/bootstrap/js/bootstrap.js"></script>
    <script>
$(document).ready(function(){
    $(".dropdown-toggle").dropdown();
});
    </script>
</body>
</html>
