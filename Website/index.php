<?php
$brand = "SteerX";
?>
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!-->
<html lang="en" class="no-js">
<!--<![endif]-->

<head>
    <meta charset="utf-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <meta name="description" content="">
    <meta name="author" content="">

    <title><?php echo $brand; ?> - An Open-Source Autonomous Car Project at Ashoka University</title>
    <!-- Standard Favicon -->
   

    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="css/animate.css">
    <link rel="stylesheet" type="text/css" href="css/normalize.css">
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link rel="stylesheet" type="text/css" href="css/swiper.min.css">
    <link rel="stylesheet" type="text/css" href="css/owl.carousel.min.css">
    <link rel="stylesheet" type="text/css" href="css/owl.theme.default.min.css">
    <link rel="stylesheet" type="text/css" href="css/magnific-popup.css">
    <link href="https://use.fontawesome.com/releases/v5.0.8/css/all.css" rel="stylesheet">

    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,600,700,900" rel="stylesheet">
    <script src="js/vendor/modernizr.js"></script>

    <!--[if lt IE 9]>
    <script src="js/html5/respond.min.js"></script>
    <![endif]-->
</head>

<body data-spy="scroll" data-target=".navbar" data-offset="60">
    
    <!-- main nav start -->

    <nav class="navbar navbar-expand-lg fixed-top center-brand static-nav">
      <div class="container">
         <a class="navbar-brand" href="#">
         <!--<img src="img/logo.png" alt="logo" class="logo-default">-->
         <font size="+3" color="#fff" style="text-transform:uppercase;"><?php echo $brand; ?></font>
         </a>
         <button class="navbar-toggler navbar-toggler-right collapsed" type="button" data-toggle="collapse" data-target="#xenav">
            <i class="fas fa-bars fa-2x"></i>
         </button>
         <div class="collapse navbar-collapse" id="xenav">
            <ul class="navbar-nav" id="container">
               <li class="nav-item">
                  <a class="nav-link active" href="#home">Home</a>
               </li>

               <li class="nav-item">
                  <a class="nav-link" href="#tech">technology</a>
               </li>
               <li class="nav-item">
                  <a class="nav-link" href="#features">Features</a>
               </li>
               
            </ul>
            <ul class="navbar-nav ml-auto">
               <li class="nav-item">
                  <a class="nav-link" href="#team">Team</a>
               </li>

              
               <li class="nav-item">
                  <a class="nav-link" href="#media">media</a>
               </li>
               <li class="nav-item">
                  <a class="nav-link" href="#contactus">contact  </a>
               </li>
            </ul>
         </div>
      </div>
      <!--/.CONTAINER-->

    </nav>
    <!-- /.navbar -->

    <!--BANNER-->
    <header class="top_banner" id="home">
        <div id="particles-js"></div>
        <div class="container">
            <div class="row h-100">
                <div class="col-md-10 align-self-center offset-md-1">
                    <div class="banner_text align-self-center">
                        <h2>we are <b><?php echo $brand;?></b></h2>
                        <p>We are awesome open-source autonomous car project developed at Ashoka University. We aim to build the cheapest self-driving car that will empower the future of self-driving cars in India.</p>
                        <div class="btn-group" id="extra_nav">
                            <a href="#contactus" class="btn">contact us</a>
                            <a href="#media" class="btn">media</a>
                        </div>
                    </div><!--/.banner_text-->
                </div>
            </div>
        </div><!--/.container-->
    </header>
    <!--/BANNER-->

    <!--ABOUT US-->
    <section class="about_us" id="about">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <div class="about_left_txt">
                        <div class="title">
                            <h3>about <b>us</b></h3>
                            <div class="underline"></div>
                            <div class="btn-group">
                                <a href="#" class="btn">our mission</a>
                                <a onclick="alert('Content Empty')"class="btn">our vision</a>
                            </div>
                        </div><!--/.title-->
                        <div class="about_txt">
                            <p align="justify">With the potential for human error removed, self-driving cars will reduce instances of accidents caused by driver error, drunk driving or distracted drivers. Once driverless cars become commonplace on our streets, it is expected that accidents are likely to fall by a whopping 90%. Average commuter times in metropolitan areas in the US are currently estimated to be around 27 minutes each way. With humans no longer involved in driving, commuters are likely to save up to an hour every day – time that will undoubtedly have many spin-off benefits from wellbeing to boosting the economy.</p>

                            <p align="justify">Every year, people living in American urban areas spend almost 7 billion hours in traffic, waste 3.1 billion gallons of fuel and lose around $160 billion due to traffic congestion. With driverless cars able to access up-to-the-minute data to help monitor traffic, as well as digital maps and other tools, they will be able to determine the fastest, most efficient route possible.</p>

                            
                        </div>
                    </div><!--/.about_left_txt-->
                </div>
                <div class="col-md-6">
                    <div class="about_right_img">
                        <img src="img/about.jpg" width="600" height="475" alt=""/>
                    </div><!--/.about_right_img-->
                </div>
            </div>
        </div><!--/.container-->
    </section>
    <!--/ABOUT US-->

    <!--SERVICES-->
    <section class="services " id="tech" >
        <div class="container">
            <div class="row">
                <div class="col-md-10">
                    <div class="title">
                        <h3>we do awesome <b>design & code</b></h3>
                        <div class="underline"></div>
                    </div><!--/.title-->
                </div>
                <div class="w-100"></div>
                <div class="col-md-4 wow animate fadeInUp">
                    <div class="service_single">
                        <img src="img/icon/do1.png" alt=""/>
                        <h4>Sophisticated Technology</h4>
                        <p>The incredibly complicated technology behind self-driving cars lets the on board computer make hundreds of calculations a second. These include how far you are from objects, current speed, behaviour of other cars, and location on the globe.</p>
                    </div><!--/.service_single-->
                </div>
                <div class="col-md-4  wow animate fadeInUp" data-wow-delay="0.1s">
                    <div class="service_single">
                        <img src="img/icon/do2.png" alt=""/>
                        <h4>Fuel Savings</h4>
                        <p>Autonomous vehicles are, to all intents and purposes, software on wheels. The technology involved in a driverless car of the future will be such that each vehicle can be optimized to ensure fuel consumption is as efficient as possible.</p>
                    </div><!--/.service_single-->
                </div>
                <div class="col-md-4  wow animate fadeInUp" data-wow-delay="0.2s">
                    <div class="service_single">
                        <img src="img/icon/do3.png" alt=""/>
                        <h4>No More Drunk Driving</h4>
                        <p>With the potential for human error removed, self-driving cars will reduce instances of accidents caused by driver error, drunk driving or distracted drivers.</p>
                    </div><!--/.service_single-->
                </div>
                <div class="col-md-4 wow animate fadeInUp">
                    <div class="service_single">
                        <img src="img/icon/do4.png" alt=""/>
                        <h4>Save Your Time</h4>
                        <p>With humans no longer involved in driving, commuters are likely to save up to an hour every day – time that will undoubtedly have many spin-off benefits from wellbeing to boosting the economy.</p>
                    </div><!--/.service_single-->
                </div>
                <div class="col-md-4 wow animate fadeInUp" data-wow-delay="0.1s">
                    <div class="service_single">
                        <img src="img/icon/do5.png" alt=""/>
                        <h4>Smart Algorithms</h4>
                        <p>With driverless cars able to access up-to-the-minute data to help monitor traffic, as well as digital maps and other tools, they will be able to determine the fastest, most efficient route possible.</p>
                    </div><!--/.service_single-->
                </div>
                <div class="col-md-4 wow animate fadeInUp" data-wow-delay="0.2s">
                    <div class="service_single">
                        <img src="img/icon/do6.png" alt=""/>
                        <h4>Influence Infrastecture</h4>
                        <p>Driverless cars will play a key role in the future of smart cities, and they will even impact the way city infrastructure is designed and built.</p>
                    </div><!--/.service_single-->
                </div>
            </div>
        </div><!--/.container-->
    </section>
    <!--/SERVICES-->


    <!--BEST FEATUERES-->
    <section class="b_features " id="features">
        <div class="container">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="title">
                        <h3>Best Features</h3>
                        <div class="underline"></div>
                    </div><!--/.title-->
                </div>
                <div class="w-100"></div>
                <div class="col-md-4  wow animate fadeInUp" >
                    <div class="single_feature">
                        <div class="feature_icon">
                            <img src="img/icon/feature1.png" class="show_icon" alt=""/>
                            <img src="img/icon/feature1hv.png" class="hide_icon" alt=""/>
                        </div><!--/.single_feature-->
                        <div class="feature_txt">
                            <h4>multi-layer CNN</h4>
                            <p>Convolutional neural network (ConvNets or CNNs) is one of the main categories to do images recognition, images classifications.</p>
                        </div>
                        <div class="line1"></div>
                        <div class="line2"></div>
                    </div><!--/.single_feature-->
                </div>
                <div class="col-md-4  wow animate fadeInUp" data-wow-delay="0.2s">
                    <div class="single_feature">
                        <div class="feature_icon">
                            <img src="img/icon/feature2.png" class="show_icon" alt=""/>
                            <img src="img/icon/feature2hv.png" class="hide_icon" alt=""/>
                        </div><!--/.single_feature-->
                        <div class="feature_txt">
                            <h4>self-training models</h4>
                            <p>Semi-supervised learning is a class of machine learning tasks and techniques that also make use of unlabeled data for training.</p>
                        </div>
                         <div class="line1"></div>
                        <div class="line2"></div>
                    </div><!--/.single_feature-->
                </div>
                <div class="col-md-4  wow animate fadeInUp" data-wow-delay="0.4s">
                    <div class="single_feature">
                        <div class="feature_icon">
                            <img src="img/icon/feature3.png" class="show_icon" alt=""/>
                            <img src="img/icon/feature3hv.png" class="hide_icon" alt=""/>
                        </div><!--/.single_feature-->
                        <div class="feature_txt">
                            <h4>speech recognition enabled</h4>
                            <p><?php echo $brand;?> develops technologies that enables the recognition and translation of language into text by computers.</p>
                        </div>
                         <div class="line1"></div>
                        <div class="line2"></div>
                    </div><!--/.single_feature-->
                </div>

                <div class="col-md-4  wow animate fadeInUp" >
                    <div class="single_feature">
                        <div class="feature_icon">
                            <img src="img/icon/feature4.png" class="show_icon" alt=""/>
                            <img src="img/icon/feature4hv.png" class="hide_icon" alt=""/>
                        </div><!--/.single_feature-->
                        <div class="feature_txt">
                            <h4>regular firmware updates</h4>
                            <p>Firmware is a software that is embedded into a hardware device. Firmware controls how your <?php echo $brand;?> device behaves.</p>
                        </div>
                         <div class="line1"></div>
                        <div class="line2"></div>
                    </div><!--/.single_feature-->
                </div>
                <div class="col-md-4  wow animate fadeInUp" data-wow-delay="0.2s">
                    <div class="single_feature">
                        <div class="feature_icon">
                            <img src="img/icon/feature5.png" class="show_icon" alt=""/>
                            <img src="img/icon/feature5hv.png" class="hide_icon" alt=""/>
                        </div><!--/.single_feature-->
                        <div class="feature_txt">
                            <h4>High accuracy models</h4>
                            <p>With accuracy of our CNN model between 72%-85%, <?php echo $brand;?> gives you the perfect, highly-accurate driving experience.</p>
                        </div>
                         <div class="line1"></div>
                        <div class="line2"></div>
                    </div><!--/.single_feature-->
                </div>
                <div class="col-md-4  wow animate fadeInUp" data-wow-delay="0.4s">
                    <div class="single_feature">
                        <div class="feature_icon">
                            <img src="img/icon/feature6.png" class="show_icon" alt=""/>
                            <img src="img/icon/feature6hv.png" class="hide_icon" alt=""/>
                        </div><!--/.single_feature-->
                        <div class="feature_txt">
                            <h4>user-friendly ux</h4>
                            <p>An elegant simplistic modular sharp flat materialistic classical design to enhance experience.</p>
                        </div>
                         <div class="line1"></div>
                        <div class="line2"></div>
                    </div><!--/.single_feature-->
                </div>
            </div>
        </div><!--/.container-->
    </section>
    <!--/BEST FEATUERES-->

   
    <!--FUN FACT-->
    <section class="fun_fact">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <div class="fun_single wow animate fadeInUp">
                        <img src="img/icon/fun1.png" alt=""/>
                        <h3>1k+ Prebookings</h3>
                        <h3>Received</h3>
                    </div><!--/.fun_single-->
                </div>
                <div class="col-md-3">
                    <div class="fun_single wow animate fadeInUp" data-wow-delay="0.1s">
                        <img src="img/icon/fun2.png" alt=""/>
                        <h3>Certified Safety</h3>
                        <h3>Standards</h3>
                    </div><!--/.fun_single-->
                </div>
                <div class="col-md-3">
                    <div class="fun_single wow animate fadeInUp" data-wow-delay="0.2s">
                        <img src="img/icon/fun3.png" alt=""/>
                        <h3>High Accuracy</h3>
                        <h3>Algorithms</h3>
                    </div><!--/.fun_single-->
                </div>
                <div class="col-md-3">
                    <div class="fun_single wow animate fadeInUp" data-wow-delay="0.3s">
                        <img src="img/icon/fun4.png" alt=""/>
                        <h3>Driverless</h3>
                        <h3>Experience</h3>
                    </div><!--/.fun_single-->
                </div>
            </div>
        </div><!--/.container-->
    </section>
    <!--/FUN FACT -->

    <!-- OUR TEAM-->
    <section class="our_team" id="team">
        <div class="container">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="title">
                        <h3>our expert team</h3>
                        <div class="underline"></div>
                        <p>Started off as Capstone Project for Advanced Programming Course at Ashoka University, <?php echo $brand; ?> is now a $1M Company.</p>
                    </div><!--/.title-->
                </div>
                <div class="w-100"></div>
                <div class="col-md-3 wow animate fadeInUp" data-wow-delay="0.1s">
                    <div class="team_single">
                        <div class="team_image">
                            <img src="img/team1.jpg" width="375" height="238" alt=""/>
                        </div><!--/.team_image-->
                        <div class="team_author">
                            <h2>Debargha Ganguly</h2>
                            <p>Machine Learning Engineer</p>
                        </div>
                    </div><!--/.team_single-->
                </div>
                <div class="col-md-3 wow animate fadeInUp" data-wow-delay="0.2s">
                    <div class="team_single">
                        <div class="team_image">
                            <img src="img/team2.jpg" width="375" height="238" alt=""/>
                        </div><!--/.team_image-->
                        <div class="team_author">
                            <h2>Prajwal Seth</h2>
                            <p>Data Science Engineer</p>
                        </div>
                    </div><!--/.team_single-->
                </div>
                <div class="col-md-3 wow animate fadeInUp" data-wow-delay="0.3s">
                    <div class="team_single">
                        <div class="team_image">
                            <img src="img/team3.jpg" width="375" height="238" alt=""/>
                        </div><!--/.team_image-->
                        <div class="team_author">
                            <h2>Shekhar Chatterjee</h2>
                            <p>CloudTech Engineer</p>
                        </div>
                    </div><!--/.team_single-->
                </div>
                <div class="col-md-3 wow animate fadeInUp" data-wow-delay="0.1s">
                    <div class="team_single">
                        <div class="team_image">
                            <img src="img/team4.jpg" width="375" height="238" alt=""/>
                        </div><!--/.team_image-->
                        <div class="team_author">
                            <h2>Sarthak Dangwal</h2>
                            <p>Creative Designer</p>
                        </div>
                    </div><!--/.team_single-->
                </div>
                
                
            </div>
        </div><!--/.container-->
    </section>
    <!-- /OUR TEAM-->

    

    
    <!--BLOG-->
    <section class="r_blog" id="media">
        <div class="container">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="title">
                        <h3>In the Media</h3>
                        <div class="underline"></div>
                        <p><?php echo $brand;?>'s extremely lost cost self-driving car technology has been featured across multiple media houses.</p>
                    </div><!--/.title-->
                </div>
                <div class="w-100"></div>
                <div class="col-md-4">
                    <div class="card">
                        <img src="img/blog1.jpg" alt="" width="375" height="245" />
                        <div class="card-body">
                            <h2>The Science of Self-Driving Cars | The Franklin Institute</h2>
                            <p>Tesla has rolled out a software system called Autopilot, which employs high-tech camera sensors as a car's “eyes,” to some...</p>
                            <a href="https://www.fi.edu/science-of-selfdriving-cars" target="_new" class="btn">read more</a>
                        </div>
                    </div><!--/.card-->
                </div>
                <div class="col-md-4">
                    <div class="card">
                        <img src="img/blog2.jpg" alt="" width="375" height="245" />
                        <div class="card-body">
                            <h2>Self-driving cars | Technology | EnterpriseAI</h2>
                            <p>A self-driving car (sometimes called an autonomous car or driverless car) is a vehicle that uses a combination of sensors...</p>
                            <a href="https://searchenterpriseai.techtarget.com/definition/driverless-car" target="_new" class="btn">read more</a>
                        </div>
                    </div><!--/.card-->
                </div>
                <div class="col-md-4">
                    <div class="card">
                        <img src="img/blog3.jpg" alt="" width="375" height="245" />
                        <div class="card-body">
                            <h2>Self-driving cars hangs on a $7 trillion problem</h2>
                            <p>I open an app. I place a dot. Minutes later, a white minivan saunters to the curb to pick me up. In the post-Uber world...</p>
                            <a href="https://www.fastcompany.com/90275407/the-fate-of-self-driving-cars-hangs-on-a-7-trillion-design-problem" target="_new" class="btn">read more</a>
                        </div>
                    </div><!--/.card-->
                </div>
            </div>
        </div><!--/.container-->
    </section>
    <!--/BLOG-->

    <!--CONTACT-->
    <section class="contacts" id="contactus">
        <div class="container">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="title">
                        <h3>contact us</h3>
                        <div class="underline"></div>
                        <p>Do you wish to collaborate with us or invest in our venture? Drop us a message or a call.</p>
                    </div><!--/.title-->
                </div>
                <div class="w-100"></div>
                <div class="col-md-12 shadow">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="contact_form">
                                <form action="https://formspree.io/shekhar.chatterjee_ug20@ashoka.edu.in" method="POST" />
                                    <div class="form-group">
                                        <label for="name1">Name</label>
                                        <input type="text" id="name1" name="name" placeholder="Your name here"/>
                                    </div>
                                    <div class="form-group">
                                        <label for="email1">Email</label>
                                        <input type="email" id="email1" name="myemail" placeholder="Your email here"/>
                                    </div>
                                    <div class="form-group">
                                        <label for="message1">Message</label>
                                        <textarea id="message1" name="message" placeholder="Your message here" cols="10" rows="3"></textarea>
                                    </div>
                                    <button type="submit">send</button>
                                </form>
                            </div><!--/.contact_form-->
                        </div>
                        <div class="col-md-5 offset-md-1">
                            <div class="contact_right_single">
                                <img src="img/icon/contact1.png" alt=""/>
                                <p>+91 - 83696 - 09636</p>
                            </div><!--/.contact_right_single-->
                            <div class="contact_right_single">
                                <img src="img/icon/contact2.png" alt=""/>
                                <p>hello@<?php echo strtolower($brand);?>.io</p>
                            </div><!--/.contact_right_single-->
                            <div class="contact_right_single">
                                <img src="img/icon/contact3.png" alt=""/>
                                <p>Centre for Entrepreneurship<br>
                                    Ashoka University, India.</p>
                            </div><!--/.contact_right_single-->
                        </div>
                    </div>
                </div>
         
            </div>
        </div><!--/.container-->
    </section>
    <!--/CONTACT-->

    <!--FOOTER-->
    <footer class="footers">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <div class="copy_right">
                        <p>© 2018 All rights reserved by <?php echo $brand;?></p>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="footer_social">
                        <ul>
                            <li><a href="#"><i class="fab fa-facebook-f"></i></a></li>
                            <li><a href="#"><i class="fab fa-twitter"></i></a></li>
                            <li><a href="#"><i class="fab fa-pinterest-p"></i></a></li>
                            <li><a href="#"><i class="fab fa-instagram"></i></a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div><!--/.container-->
    </footer>
    <!--/FOOTER-->

    <a href="#" class="scrollup"><i class="fas fa-arrow-up fa-2x"></i></a>

    



    <script src="js/jquery-1.12.4.min.js"></script>
    <script src="js/vendor/bootstrap.min.js"></script>
    <script src="js/vendor/popper.min.js"></script>
    <script src="js/vendor/plugin.js"></script>
    <script src="js/main.js"></script>

     

</body>
</html>