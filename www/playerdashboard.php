<?php
include('dbphpconnect.php');

$keyplayer = htmlspecialchars($_GET["playerid"]);
#$sqlHeader = "Call GetPlayerHeader(". $keyplayer . ")";
$sql = "Call GetPlayerGameStats(" . $keyplayer . ");";
$sql .= "Call GetPlayerHeader(" . $keyplayer . ");";

$outp = [];
$header = [];
if (mysqli_multi_query($conn, $sql)) {
	do {
		
		if ($result=mysqli_store_result($conn)) {
			while ($row = mysqli_fetch_assoc($result)) {
				if (isset($row['keygame'])) {	
					$outp[] = ['keygame'=>(int)$row['keygame'], 'opponent'=>$row['teamshort'], 'gametime'=>$row['gametime'], 'points'=>(int)$row['points']];				
				}
				if (isset($row['name'])) {
					$header[] = ['name'=>$row['name'], 'teamlong'=>$row['teamlong'], 'recentyear'=>(int)$row['recentyear'], 'firstyear'=>(int)$row['firstyear']];
				}				
			}
			mysqli_free_result($result);
		}
	}
	while (mysqli_next_result($conn));
}
$playerHeaderArray = (array)$header;

?>
<!DOCTYPE html>
<meta charset="UTF-8">
<head>
<script src="https://d3js.org/d3.v4.min.js"></script>
<style>
.bar {
  	fill: red;
}
.bar:hover{
	fill:black;
}

.axis text {
  font: 10px sans-serif;
}

.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}

.x.axis path {
  display: none;
}

</style>
</head>
<body>
	<!--<div class="chart"></div>-->
	<h1><?php echo $playerHeaderArray[0]['name']; ?></h1>
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
var margin = {top: 20, right: 30, bottom: 30, left: 40},
    width = 1100 - margin.left - margin.right,
    height = 350 - margin.top - margin.bottom;

var x = d3.scaleBand()
    .rangeRound([0, width], .1);

var y = d3.scaleLinear()
    .range([height, 0]);
    
var xAxis = d3.axisBottom(x);

var yAxis = d3.axisLeft(y);



var chart = d3.select(".chart")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

x.domain(data.map(function(d) { return d.opponent; }));
y.domain([0, d3.max(data, function(d) { return d.points; })]);

chart.append("g")
  .attr("class", "x axis")
  .attr("transform", "translate(0," + height + ")")
  .call(xAxis);

chart.append("g")
  .attr("class", "y axis")
  .call(yAxis);
   
chart.selectAll(".bar")
  .data(data)
 .enter().append("rect")
  .attr("class", "bar")
  .attr("x", function(d) { return x(d.opponent); })
  .attr("y", function(d) { return y(d.points); })
  .attr("height", function(d) { return height - y(d.points); })
  .attr("width", x.bandwidth());
    
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
