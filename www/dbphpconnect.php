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
$sql = "SELECT keygame, points FROM gamestats where keyplayer = 4066372";
$result = $conn->query($sql);

if ($result-> num_rows == 0) {
	echo 'No results from db.';
}
$outp = [];
while($row = $result->fetch_assoc()) {
	$outp[] = ['keygame'=>(int)$row['keygame'], 'points'=>(int)$row['points']];
}

// $first = reset($outp);
// print_r($first);
// echo json_encode($outp);

?>
<!DOCTYPE html>
<meta charset="UTF-8">
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

.chart rect {
  fill: steelblue;
}

.chart text {
  fill: white;
  font: 10px sans-serif;
  text-anchor: end;
}

</style>
</head>
<body>
	<!--<div class="chart"></div>-->
	<svg class="chart"></svg>
<script>
var data = <?php echo json_encode($outp); ?>;
/* Tutorial Part 1 Bar Chart HTML
var x = d3.scaleLinear()
    .domain([0, d3.max(data)])
    .range([0, 420]);


d3.select(".chart")
  .selectAll("div")
    .data(data)
  .enter().append("div")
    .style("width", function(d) { return x(d) + "px"; })
    .text(function(d) { return d; });
End of Part 1*/

/*Part 2 */
var width = 420,
    barHeight = 20;

var x = d3.scaleLinear()
    .range([0, width]);

var chart = d3.select(".chart")
    .attr("width", width);

x.domain([0, d3.max(data, function(d) { return d.points; })]);

chart.attr("height", barHeight * data.length);

var bar = chart.selectAll("g")
  .data(data)
.enter().append("g")
  .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

bar.append("rect")
  .attr("width", function(d) { return x(d.points); })
  .attr("height", barHeight - 1);

bar.append("text")
  .attr("x", function(d) { return x(d.points) - 3; })
  .attr("y", barHeight / 2)
  .attr("dy", ".35em")
  .text(function(d) { return d.points; });
    
</script>
<!--
<svg class="chart" width="420" height="120">
  <g transform="translate(0,0)">
    <rect width="40" height="19"></rect>
    <text x="37" y="9.5" dy=".35em">4</text>
  </g>
  <g transform="translate(0,20)">
    <rect width="80" height="19"></rect>
    <text x="77" y="9.5" dy=".35em">8</text>
  </g>
  <g transform="translate(0,40)">
    <rect width="150" height="19"></rect>
    <text x="147" y="9.5" dy=".35em">15</text>
  </g>
  <g transform="translate(0,60)">
    <rect width="160" height="19"></rect>
    <text x="157" y="9.5" dy=".35em">16</text>
  </g>
  <g transform="translate(0,80)">
    <rect width="230" height="19"></rect>
    <text x="227" y="9.5" dy=".35em">23</text>
  </g>
  <g transform="translate(0,100)">
    <rect width="420" height="19"></rect>
    <text x="417" y="9.5" dy=".35em">42</text>
  </g>
</svg>-->
</body>
</html>
