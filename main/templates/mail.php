<?php
	require 'phpmailer/PHPMailerAutoload.php';
    require 'admin/classes/config.php';

        $name = $_REQUEST['name'];
        $email = $_REQUEST['email'];
        $subject = $_REQUEST['subject'];
        $mess = $_REQUEST['mess'];
        $message = '
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>'.$subject.'</title>
        </head>
        <body>
            <p>
                '.$mess.'
            </p>
        </body>
        </html>
        ';
        $mail = new PHPMailer;
        $mail->SMTPDebug = 4;
        $mail->isSMTP();
        $mail->Host       = MHOST;
        $mail->SMTPAuth   = true;
        $mail->Username   = EMAIL;
        $mail->Password   = MPASS;
        $mail->SMTPSecure = 'tls';
        $mail->Port       = 587;
        $mail->setFrom( $email,$name );
        $mail->addAddress(EMAIL);
        $mail->addReplyTo( $email,$name );
        $mail->isHTML( true );
        $mail->Subject   = $subject;
        $mail->Body      = $message;
        $mail->AltBody   = "Customer Message";
        header("location:thank-you");
        $send            = $mail->send();
        
        
    
    // elseif(isset($_REQUEST['subscribe'])){
    //     $email_add = $_REQUEST['subscribe'];
    //     $token = sha1(md5($email_add));
    //     $subject = 'verify your Email';
    //     $name = "creative-Azad";
    //     $massage = '
    //    <!DOCTYPE html>
    //     <html lang="en">
    //     <head>
    //         <meta charset="UTF-8">
    //         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    //         <title>Verify your email</title>
    //     </head>
    //     <body>
    //         <p>
    //             Thank you for subscribing us. please click on the link below to verify your email.
    //         </p>
    //         <a href="https://azad.creative-jfa.com/creative/core/sub_core.php?sub_token='.$token.'">verify email adders</a>
    //     </body>
    //     </html>
    //     ';
    //     $mail = new PHPMailer;
    //     $mail->SMTPDebug = 4;
    //     $mail->isSMTP();
    //     $mail->Host       = HOST;
    //     $mail->SMTPAuth   = true;
    //     $mail->Username   = EMAIL;
    //     $mail->Password   = PASS;
    //     $mail->SMTPSecure = 'ssl';
    //     $mail->Port       = 465;
    //     $mail->setFrom( EMAIL,$name );
    //     $mail->addAddress($email_add);
    //     $mail->addReplyTo( 'freelancerazad47@gmail.com' );
    //     $mail->isHTML( true );
    //     $mail->Subject   = $subject;
    //     $mail->Body      = $massage;
    //     $mail->AltBody   = "Verification message!";
    //     header('location:../index');
    //     $send            = $mail->send();
        
    // }
    

   
// if(isset($_POST['submit']))
// {
//     $result = "";
//     $error  = "";
//     require 'phpmailer/PHPMailerAutoload.php';
//     $mail = new PHPMailer;
//     //smtp settings
//     $mail->isSMTP(); // send as HTML
//     $mail->Host = "smtp.gmail.com"; // SMTP servers
//     $mail->SMTPAuth = true; // turn on SMTP authentication
//     $mail->Username = "your email"; // Your mail
//     $mail->Password = 'your password'; // Your password mail
//     $mail->Port = 587; //specify SMTP Port
//     $mail->SMTPSecure = 'tls';                               
//     $mail->setFrom($_POST['email'],$_POST['name']);
//     $mail->addAddress('your email');
//     $mail->addReplyTo($_POST['email'],$_POST['name']);
//     $mail->isHTML(true);
//     $mail->Subject='Form Submission:' .$_POST['subject'];
//     $mail->Body='<h3>Name :'.$_POST['name'].'<br> Email: '.$_POST['email'].'<br>Message: '.$_POST['message'].'</h3>';
//     if(!$mail->send())
//     {
//         $error = "Something went worng. Please try again.";
//     }
//     else 
//     {
//         $result="Thanks\t" .$_POST['name']. " for contacting us.";
//     }
// }
?>