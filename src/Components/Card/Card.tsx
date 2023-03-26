import "./Card.css"

const Card = ({key, author, author_img, date_time, text, imgs}:any) => {
    // console.log(author, author_img, date_time, text, imgs)
    let imgsArr = []
    if (imgs)
        imgsArr = imgs.split(' ')
    // console.log(imgsArr)
    if (imgsArr.length > 0 && imgsArr.at(-1).length === 0)
        imgsArr.splice(imgsArr.length-1, 1)

    return(
        <div className="card-container" key={key}>
            <div className="card-author-container">
                <img src={author_img} className="card-author-img"/>
                <div className="card-author-wrapper">
                    <p className="card-author">{author}</p>
                    <p className="card-date-time">{date_time}</p>
                </div>
            </div>
            <div className="card-imgs-containesr">
                <div className={"card-imgs-wrapper"}>
                    { imgsArr && imgsArr.length? 
                        imgsArr.map((link:string, idx:number)=>
                            <img 
                                key={idx}
                                src={link}
                                className={"card-img" + (imgsArr.length===1? " lone-img":"")}
                            />
                        )
                    :<></>}
                </div>
            </div>
            <p className={"card-text" + (imgsArr.length===0 ? " lone-text":"")}>{text}</p>
        </div>
    );
}

export default Card;