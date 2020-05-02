<?php

if (isset($_POST['submit'])){
    
    $name = $_POST['name'];
    $subject = $_POST['subject'];
    $mailFrom = $_POST['email'];
    $message = $_POST['message'];

    $mailTo = "deportationsquadvum@gmail.com";
    $txt = "You have received an email from ".$name." ".$mailFrom.".\n\n".$message;

    mail($mailTo,$subject, $txt);
    header("Location: index.html?mailsend");
}

?>