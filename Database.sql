CREATE DATABASE csdl_bit;
CREATE TABLE csdl_bit.Users (
  id varchar(50) PRIMARY KEY,
  username varchar(50),
user_password varchar(225),
  email varchar(50),
  phone varchar(50),
  age integer,
  department varchar(50)
);

CREATE TABLE csdl_bit.Documents (
  document_id varchar(50) PRIMARY KEY,
  title varchar(50),
  content text COMMENT 'Content of the post',
  password text,
  uploaded_by varchar(50)
);

CREATE TABLE csdl_bit.Tags (
  tag_id varchar(50) PRIMARY KEY,
  nameposts_tags  varchar(255)
);

CREATE TABLE csdl_bit.Posts (
  post_id varchar(50) PRIMARY KEY,
  title text,
  content text,
  posted_by varchar(50)
);

CREATE TABLE csdl_bit.Ratings (
  rating_id varchar(50) PRIMARY KEY,
  star_rating int,
  rated_by varchar(50),
  document_id varchar(50)
);

CREATE TABLE csdl_bit.Comments (
  comment_id varchar(50) PRIMARY KEY,
  content text,
  commented_by varchar(50),
  post_id varchar(50),
  document_id varchar(50)
);

CREATE TABLE csdl_bit.Posts_tags (
  post_id varchar(50),
  tag_id varchar(50),
  PRIMARY KEY (post_id, tag_id)
);

CREATE TABLE csdl_bit.Documents_tags (
  document_id varchar(50),
  tag_id varchar(50),
  PRIMARY KEY (document_id, tag_id)
);

CREATE TABLE csdl_bit.Bookmarks (
  document_id varchar(50),
  user_id varchar(50),
  PRIMARY KEY (document_id, user_id)
);

ALTER TABLE csdl_bit.Documents ADD FOREIGN KEY (uploaded_by) REFERENCES csdl_bit.Users (id);

ALTER TABLE csdl_bit.Posts ADD FOREIGN KEY (posted_by) REFERENCES csdl_bit.Users (id);

ALTER TABLE csdl_bit.Ratings ADD FOREIGN KEY (rated_by) REFERENCES csdl_bit.Users (id);

ALTER TABLE csdl_bit.Ratings ADD FOREIGN KEY (document_id) REFERENCES csdl_bit.Documents (document_id);

ALTER TABLE csdl_bit.Comments ADD FOREIGN KEY (commented_by) REFERENCES csdl_bit.Users (id);

ALTER TABLE csdl_bit.Comments ADD FOREIGN KEY (document_id) REFERENCES csdl_bit.Documents (document_id);

ALTER TABLE csdl_bit.Comments ADD FOREIGN KEY (post_id) REFERENCES csdl_bit.Posts (post_id);

ALTER TABLE csdl_bit.Posts_tags ADD FOREIGN KEY (post_id) REFERENCES csdl_bit.Posts (post_id);

ALTER TABLE csdl_bit.Posts_tags ADD FOREIGN KEY (tag_id) REFERENCES  csdl_bit.Tags (tag_id);

ALTER TABLE csdl_bit.Documents_tags ADD FOREIGN KEY (document_id) REFERENCES csdl_bit.Documents (document_id);

ALTER TABLE csdl_bit.Documents_tags ADD FOREIGN KEY (tag_id) REFERENCES  csdl_bit.Tags (tag_id);

ALTER TABLE csdl_bit.Bookmarks ADD FOREIGN KEY (document_id) REFERENCES csdl_bit.Documents (document_id);

ALTER TABLE csdl_bit.Bookmarks ADD FOREIGN KEY (user_id) REFERENCES csdl_bit.Users (id);
