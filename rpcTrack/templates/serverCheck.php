<?php   
include ("connect.php");
session_start();

$username = $_POST['username'];
$email = $_POST['email'];

$email = mysqli_real_escape_string($con, $_POST['email']);

$query1 = "SELECT * FROM registration where (email='$email')";
$check = mysqli_query($con, $query1);
$checkrows=mysqli_num_rows($check);

if($checkrows>0) {
echo json_encode(FALSE);
}
else
{
echo json_encode(TRUE);
}

//insert results from the form input
$query = "INSERT INTO registration (username, email) VALUES('$username', '$email')";
$result = mysqli_query($con, $query);
$num1=mysqli_num_rows($result);
$row = mysqli_fetch_assoc($result);

?>