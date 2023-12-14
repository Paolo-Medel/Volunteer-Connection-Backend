import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { RetrieveOpportunities } from "../services/opportunitiesService";
import { getCauseAreas } from "../services/causeAreaService";

export const EditOpportunity = () => {
  const [causes, setCauses] = useState([]);
  const [chosenCauses, updateChosen] = useState(new Set());
  const [editedPost, setEditedPost] = useState({
    title: "",
    image_url: "",
    content: "",
    cause_area: [],
  });

  const { postId } = useParams();
  const navigate = useNavigate();

  const handleCauseChosen = (cause) => {
    const copy = new Set(chosenCauses);
    copy.has(cause.id) ? copy.delete(cause.id) : copy.add(cause.id);
    updateChosen(copy);
  };

  useEffect(() => {
    RetrieveOpportunities(postId).then((obj) => {
      setEditedPost(obj);
    });

    getCauseAreas().then((obj) => {
      setCauses(obj);
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
      <fieldset className="flex flex-wrap gap-4">
        {causes.map((c) => (
          <div className="flex items-center" key={c.id}>
            <input
              className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
              type="checkbox"
              checked={editedPost.cause_area.some((obj) => obj.id === c.id)}
              onChange={() => {
                handleCauseChosen(c);
              }}
            />
            <div className="ms-2 text-sm text-white">{c.label}</div>
          </div>
        ))}
      </fieldset>
      <button type="submit" className="btn-edit mb-4">
        Save Changes
      </button>
    </form>
  );
};

//   editedPost.cause_area.map((obj) => {
//     if (obj.id === c.id) {
//       return true;
//     } else return false;
//   })
