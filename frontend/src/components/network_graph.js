// import AnyChart from 'anychart';
import AnyChart from 'anychart-react'
import anychart from 'anychart'
import React, { useEffect } from 'react';

function NetworkGraph(props){
    useEffect(() => {
        // create data
        var nodes = props.data.data.map(([id]) => ({ id, group:'similar' }));
        // console.log(nodes)
        nodes = [...nodes, { id: props.data.search, group:'search' }];
        const dataToEdges = (searchTerm, dataArray) => {
            const result = dataArray
            .map(([name, value]) => ({ from: searchTerm, to: name}));
            return result;
        };
      
        const edges = dataToEdges(props.data.search, props.data.data);
    
        var data = {
            nodes: nodes,
            edges: edges,
        };
  
        // create a chart and set the data
        var chart = anychart.graph(data);

        var nodes = chart.nodes();

        nodes.normal().height(40);
        nodes.hovered().height(55);
        nodes.selected().height(55);
    
        // enable labels of nodes
        chart.nodes().labels().enabled(true);

        // configure labels of nodes
        chart.nodes().labels().format("{%id}");
        chart.nodes().labels().fontSize(15);
        chart.nodes().labels().fontWeight(600);
        

        chart.group("similar").normal().fill('#f49f59')

        // render chart to the specified container
        chart.container('chart-container');
        chart.draw();
  
        // Clean up the chart when the component unmounts
        return () => chart.dispose();
    }, []); // Empty dependency array to ensure useEffect runs only once
  
    return <div id="chart-container" style={{ width: '100%', height: '500px' }} />;
  };
  
export default NetworkGraph;