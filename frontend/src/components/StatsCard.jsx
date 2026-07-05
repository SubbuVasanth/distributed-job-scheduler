function StatsCard({title, value, color}){
    return(
        <div className="col-md-4">
            <div className={`stats-card-container glass-panel stat-${color}`}>
                <h6>{title}</h6>
                <h2>{value}</h2>
            </div>
        </div>
    )
}

export default StatsCard;