(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['exports', 'echarts'], factory);
    } else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {
        // CommonJS
        factory(exports, require('echarts'));
    } else {
        // Browser globals
        factory({}, root.echarts);
    }
}(this, function (exports, echarts) {
    var log = function (msg) {
        if (typeof console !== 'undefined') {
            console && console.error && console.error(msg);
        }
    }
    if (!echarts) {
        log('ECharts is not Loaded');
        return;
    }
    if (!echarts.registerMap) {
        log('ECharts Map is not loaded')
        return;
    }
    echarts.registerMap('cstmap',{
      "type": "FeatureCollection",
      "features": [{
        "type": "Feature",
        "properties": {"name":"A"},
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [106.600341796875, 26.066652138577403],
              [107.193603515625, 25.46311452925943],
              [109.171142578125, 27.068909095463365],
              [107.38037109375, 27.264395776495334],
              [106.600341796875, 26.066652138577403]
            ]
          ]
        }
      }, {
        "type": "Feature",
        "properties": {"name":"C"},
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [107.259521484375, 25.34402602913433],
              [109.05029296875, 24.896402266558727],
              [110.819091796875, 26.765230565697482],
              [109.281005859375, 26.980828590472107],
              [107.259521484375, 25.34402602913433]
            ]
          ]
        }
      }, {
        "type": "Feature",
        "properties": {"name":"B"},
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [107.42431640625, 27.44004046509707],
              [109.281005859375, 27.479034752500656],
              [110.028076171875, 28.333395169196457],
              [109.0283203125, 28.507315578441784],
              [107.42431640625, 27.44004046509707]
            ]
          ]
        }
      }, {
        "type": "Feature",
        "properties": {"name":"D"},
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [109.83032226562499, 27.42053815128712],
              [111.697998046875, 26.980828590472107],
              [112.06054687499999, 27.9361805667694],
              [110.654296875, 28.13981591275445],
              [109.83032226562499, 27.42053815128712]
            ]
          ]
        }
      }]
    }
)
  }));
