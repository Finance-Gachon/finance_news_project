// import AnyChart from 'anychart';
import AnyChart from 'anychart-react'

function WordCloud(props) {

    const data = props.data.map(([x, value]) => ({ x, value }))

    return (
        <div>
            <AnyChart
                id="TagCloud"
                width={600}
                height={450}
                type="tagCloud"
                mode="rect"
                angles={[0]}
                data={data}
                title="워드 클라우드"
            />
        </div>
    )
}

export default WordCloud;