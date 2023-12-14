import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { RetrieveOpportunities } from "../services/opportunitiesService";
import { getCauseAreas } from "../services/causeAreaService";

export const EditOpportunity = () => {
  const [cause, setCause] = useState([]);
  const [editedPost, setEditedPost] = useState({});

  const { postId } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    RetrieveOpportunities(postId).then((obj) => {
      setEditedPost(obj);
    });

    getCauseAreas().then((obj) => {
      setCause(obj);
    });
  }, []);

  const handleInputChange = (event) => {
    setEditedPost({ ...editedPost, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    await fetch(`http://localhost:8000/posts/${postId}`, {
      method: "PUT",
      headers: {
        Authorization: `Token ${
          JSON.parse(localStorage.getItem("volunteer_token")).token
        }`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(editedPost),
    });
    navigate(`/posts/${postId}`);
  };

  return (
    <>
      <form
        onSubmit={handleSubmit}
        className="flex flex-col items-start gap-4 w-9/12 bg-sky-700/80 px-6 rounded-md border border-white/60"
      >
        <header>
          <div className="text-3xl font-bold text-white my-4">Edit Post</div>
        </header>
        <fieldset>
          <div>
            <input
              name="title"
              placeholder="Title"
              className="input-text w-[512px]"
              value={editedPost.title}
              type="text"
              onChange={handleInputChange}
            />
          </div>
        </fieldset>
        <fieldset>
          <div>
            <input
              name="image_url"
              placeholder="Image URL"
              value={editedPost.image_url}
              className="input-text w-[512px]"
              type="text"
              onChange={handleInputChange}
            />
          </div>
        </fieldset>
        <fieldset>
          <div>
            <textarea
              name="content"
              className="input-text w-[512px] h-[128px]"
              placeholder="Article Content"
              value={editedPost.content}
              onChange={handleInputChange}
            />
          </div>
        </fieldset>
        <fieldset>
          <select
            name="category"
            onChange={handleInputChange}
            className="rounded p-2 text-sm"
            value={editedPost.category}
          >
            <option value={0}>Category Select</option>
            {cause.map((c) => {
              return (
                <option key={c.id} value={c.id}>
                  {c.label}
                </option>
              );
            })}
          </select>
        </fieldset>
        <fieldset className="flex flex-wrap gap-4">
          {cause.map((c) => (
            <div key={c.id} value={c.id} className="flex items-center">
              <input
                className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                type="checkbox"
                name="category"
                onChange={handleInputChange}
                value={editedPost.category}
              />
              <div className="ms-2 text-sm text-white">{c.label}</div>
            </div>
          ))}
        </fieldset>
        <button type="submit" className="btn-edit mb-4">
          Save Changes
        </button>
      </form>
    </>
  );
};