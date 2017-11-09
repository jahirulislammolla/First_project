<!doctype html>  
<html>  
<head>  
<title>Login</title>  
<link rel="stylesheet" type="text/css" href="style.css"> 
</head>  
<body>  
    <center><h3>CREATE REGISTRATION AND LOGIN FORM</h3></center>  
    <p><a href="register">Register</a> | <a href="login">Login</a></p>  
    <h3>Login Form</h3>  
    <form action="" method="POST">  
    Username: <input type="text" placeholder="enter your username" name="user"><br />  
    Password: <input type="password"  placeholder="entet your password" name="pass"><br />   
    <input type="submit" value="Login" name="submit" />  
    </form>  
    <?php  
        if(isset($_POST["submit"])){  
          
        if(!empty($_POST['user']) && !empty($_POST['pass'])) {  
            $user=$_POST['user'];  
            $pass=$_POST['pass'];   
            }  
        else  
            echo "All fields are required!";
            }
    ?>  
</body>  
</html>