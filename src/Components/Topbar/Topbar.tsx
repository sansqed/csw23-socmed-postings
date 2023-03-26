import React from "react"
import "./Topbar.css"
import logo from "../../Assets/komsai-week.png"
import config from "../../config.json"

const Topbar = ({hashtag}:any) => {
    const hashtags = config.HASHTAGS
    // console.log(hashtags)
    return(
        <div className="topbar-container">
            <img src={logo} className="topbar-logo"/>
            <p className="topbar-hashtag">{hashtags.map((h, idx)=>" #"+h+ (idx!==hashtags.length-1? ' |':""))}</p>
        </div>
    )

}

export default Topbar;