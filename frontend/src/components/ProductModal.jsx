import { useState, useEffect } from "react";

import api from "../api";


const ProductModal = ({ product, onClose, type }) => {
  if (!product) return null;
  
  const [imageUrl, setImageUrl] = useState("");
  const img_url = `http://127.0.0.1:8000/${type}s/get_one?title=` + product.title_wos;

  useEffect(() => {
      api.get(img_url, {
          responseType: 'blob'
      })
      .then(response => {
          const url = URL.createObjectURL(response.data);
          setImageUrl(url);
      })
      .catch(error => console.error('Error fetching image:', error));
  }, []);

  return (
    <div className="modal" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        
        <div className='modal-image' style={{
              backgroundImage: `url(${imageUrl})`,
              backgroundSize: 'cover',
              backgroundPosition: 'center',
              backgroundRepeat: 'no-repeat'
            }
        }></div>

        <div className="modal-info">
          <h2>{product.title}</h2>

          <span>{type}</span>
          <p>{product.fullDescription}</p>

          <div className="modal-details">
            <h2><strong>Price:</strong> {product.price}</h2>
            <p>{product.description}</p>
            
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductModal;
