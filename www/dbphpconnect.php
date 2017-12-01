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
$sql = "SELECT points FROM gamestats where keyplayer = 4066372";
$result = $conn->query($sql);

if ($result-> num_rows > 0) {
	echo "so many records";
}

else {
	echo "no results";
}
$outp = array();
while($row = $result->fetch_assoc()) {
	$outp[] = $row['points'];
}
//print_r($outp);
//echo json_encode($outp);

?>
<!DOCTYPE html>
<head>
<script src="https://d3js.org/d3.v4.min.js"></script>
<style>
.chart div {
  font: 10px sans-serif;
  background-color: steelblue;
  text-align: right;
  padding: 3px;
  margin: 1px;
  color: white;
}
</style>
</head>
<body>
	<div class="chart">
	<?php echo implode($outp, ','); ?>
	</div>
<script>
var data = <?php echo '[' . implode($outp, ',') , ']'; ?>;

var x = d3.scaleLinear()
    .domain([0, d3.max(data)])
    .range([0, 420]);

d3.select(".chart")
  .selectAll("div")
    .data(data)
  .enter().append("div")
    .style("width", function(d) { return x(d) + "px"; })
    .text(function(d) { return d; });
</script>
</body>
</html>

<?php

?>