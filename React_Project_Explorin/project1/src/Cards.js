import "./App.css";
function GroupExample(post) {
  return (
    <div className="post-card">
      <img
        className="rounded-t-lg"
        src={`https://robohash.org/${post.id}`}
        alt=""
      />
      <h2>{post.name}</h2>
      <h4 className="post-title">{post.username}</h4>
      <p className="post-body">{post.email}</p>
    </div>
  );
}

export default GroupExample;
