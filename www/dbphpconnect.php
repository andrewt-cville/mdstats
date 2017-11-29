<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "mdstats";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";

$sql = "SELECT * FROM teams";
$result = $conn->query($sql);

if ($result-> num_rows > 0) {
	echo "so many records";
}

else {
	echo "no results";
}
$outp = array();
$outp = $result->fetch_all(MYSQLI_ASSOC);

echo json_encode($outp);
echo "hello";
?>