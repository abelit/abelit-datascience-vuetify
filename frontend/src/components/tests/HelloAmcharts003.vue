<template>
  <div id="chartdiv"></div>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import am4themes_dataviz from "@amcharts/amcharts4/themes/dataviz";

// Themes begin
am4core.useTheme(am4themes_dataviz);
am4core.useTheme(am4themes_animated);
// Themes end
export default {
  name: 'HelloAmcharts',
  mounted () {
    var chart = am4core.create("chartdiv", am4charts.ChordDiagram);
chart.hiddenState.properties.opacity = 0;

var data = [];
var letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

function randomLetter(except) {
    var letter = letters[Math.floor(Math.random() * letters.length - 1)];
    if (letter == except) {
        return randomLetter(except);
    }
    else {
        return letter;
    }
}

for (var i = 0; i < letters.length; i++) {
    var fromLetter = letters[i];
    for (var o = 0; o < 3; o++) {
        data.push({ from: fromLetter, to: randomLetter(fromLetter), value: Math.round(Math.random() * 100) });
    }
}

chart.data = data;

chart.dataFields.fromName = "from";
chart.dataFields.toName = "to";
chart.dataFields.value = "value";
chart.nonRibbon = true;
chart.sortBy = "name";
chart.startAngle = 90;
chart.endAngle = 450;

var nodeTemplate = chart.nodes.template;
nodeTemplate.fill = chart.colors.getIndex(0);
nodeTemplate.fillOpacity = 0.4;
nodeTemplate.slice.disabled = true;
nodeTemplate.setStateOnChildren = true;
nodeTemplate.label.disabled = true;
nodeTemplate.togglable = false;

nodeTemplate.readerTitle = "Drag to rearrange";
nodeTemplate.showSystemTooltip = true;

var hoverState = nodeTemplate.states.create("hover");
hoverState.properties.fillOpacity = 1;

var linkTemplate = chart.links.template;
linkTemplate.opacity = 0.1;
linkTemplate.stroke = chart.colors.getIndex(0);
linkTemplate.defaultState.properties.opacity = 0.1;
linkTemplate.tooltipText = "";

var linkHoverState = linkTemplate.states.create("hover");
linkHoverState.properties.opacity = 1;

nodeTemplate.events.on("over", function (event) {
    var node = event.target;
    node.outgoingDataItems.each(function (dataItem) {
        dataItem.link.isHover = true;
    })
})

nodeTemplate.events.on("out", function (event) {
    var node = event.target;
    node.outgoingDataItems.each(function (dataItem) {
        dataItem.link.isHover = false;
    })
})

nodeTemplate.cursorOverStyle = am4core.MouseCursorStyle.grab;

nodeTemplate.cursorDownStyle = am4core.MouseCursorStyle.grabbing;

var circleBullet = nodeTemplate.createChild(am4charts.CircleBullet);
circleBullet.setStateOnChildren = true;
circleBullet.circle.radius = 15;

var circleHoverState = circleBullet.states.create("hover");
circleHoverState.properties.scale = 1.5;

// we create a separate label as node.label ispositioned differently and doesn't fit perfectly for one-letter labels
var label = circleBullet.createChild(am4core.Label);
label.text = "{fromName}";
label.horizontalCenter = "middle";
label.verticalCenter = "middle";

var labelHoverState = label.states.create("hover");
labelHoverState.properties.fill = am4core.color("#ffffff");
  },
  beforeDestroy () {
    if (this.chart) {
      this.chart.dispose;
    }
  }
  }
</script>

<style lang="css" scoped>
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}

#chartdiv {
  width: 100%;
  height: 700px;
}
</style>
