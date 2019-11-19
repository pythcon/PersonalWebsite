<?php
session_start();
include ('account.php');
include ('functions.php');

gatekeeper();


?>
<!DOCTYPE html>
<!--[if IE 8 ]><html class="no-js oldie ie8" lang="en"> <![endif]-->
<!--[if IE 9 ]><html class="no-js oldie ie9" lang="en"> <![endif]-->
<!--[if (gte IE 9)|!(IE)]><!--><html class="no-js" lang="en"> <!--<![endif]-->
<head>

   <!--- basic page needs
   ================================================== -->
   <meta charset="utf-8">
	<title>Todd Murphy</title>
	<meta name="description" content="">  
	<meta name="author" content="">

   <!-- mobile specific metas
   ================================================== -->
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

 	<!-- CSS
   ================================================== -->
   <link rel="stylesheet" href="css/base.css">  
   <link rel="stylesheet" href="css/main.css">
   <link rel="stylesheet" href="css/vendor.css">     

   <!-- script
   ================================================== -->   
	<script src="js/modernizr.js"></script>
	<script src="js/pace.min.js"></script>

   <!-- favicons
	================================================== -->
	<link rel="icon" type="image/png" href="favicon.png">
    
    <!-- AJAX
	================================================== -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>

</head>

<body id="top">

	<!-- header 
   ================================================== -->
   <header>   	
   	<div class="row">
   		
   	</div> <!-- /row --> 		
   </header> <!-- /header -->

	<!-- intro section
   ================================================== -->
   <section id="intro">   

   	<div class="intro-overlay"></div>	

   	<div class="intro-content">
   		<div class="row">

   			<div class="col-twelve">

	   			<h5>Project Management</h5>
                <br>
                <div class="infoForm">
                    <h3>Management Console</h3>
                    <p>Welcome to the management console.
                        <br>
                        Please log in.
                    </p>
                    
                </div>
	   			<div class="loginForm">
                    <form action="handler.php" method="post">
                            <label>Username</label>
                            <input type="text" name="user">
                            <label>Password</label>
                            <input type="password" name="pass">
                        <br>
                            <input type="submit" name="submit" value="Login">
                    </form>
                </div>

	   		</div>  
   			
   		</div>   		 		
   	</div> <!-- /intro-content --> 

   	<ul class="intro-social">        
          <li><a href="https://www.facebook.com/todd.murphy.376"><i class="fa fa-facebook"></i></a></li>
          <li><a href="https://www.linkedin.com/in/tmurphy605"><i class="fa fa-linkedin"></i></a></li>
          <li><a href="https://github.com/tmurphy605"><i class="fa fa-github"></i></a></li>
      </ul> <!-- /intro-social -->      	

   </section> <!-- /intro -->

   <!-- footer
   ================================================== -->

   <footer>
     	<div class="row">

     		<div class="col-six tab-full pull-right social">

     			<ul class="footer-social">        
			      <li><a href="https://www.facebook.com/todd.murphy.376"><i class="fa fa-facebook"></i></a></li>
			      <li><a href="https://www.linkedin.com/in/tmurphy605"><i class="fa fa-linkedin"></i></a></li>
                  <li><a href="https://github.com/tmurphy605"><i class="fa fa-github"></i></a></li>
			   </ul> 
	      		
	      </div>

      	<div class="col-six tab-full">
	      	<div class="copyright">
		        	<span>© Copyright Kards 2016.</span> 
		        	<span>Design by <a href="http://www.styleshout.com/">styleshout</a></span>	         	
		         </div>		                  
	      	</div>

	      	<div id="go-top">
		         <a class="smoothscroll" title="Back to Top" href="#top"><i class="fa fa-long-arrow-up"></i></a>
		      </div>

      	</div> <!-- /row -->     	
   </footer>  

   <div id="preloader"> 
    	<div id="loader"></div>
   </div> 

   <!-- Java Script
   ================================================== --> 
   <script src="js/jquery-2.1.3.min.js"></script>
   <script src="js/plugins.js"></script>
   <script src="js/main.js"></script>
   <script src="js/navbar.js"></script>
   <script src="js/projects.js"></script>

</body>

</html>