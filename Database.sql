CREATE DATABASE csdl_bit;
CREATE TABLE csdl_bit.users (
  id_user char(10) PRIMARY KEY,
  username varchar(255),
  email varchar(255),
  phone char(10),
  age integer,
  department varchar(255)
);

CREATE TABLE csdl_bit.documents (
  id_document char(10) PRIMARY KEY,
  title varchar(255),
  content text COMMENT 'Content of the post',
  uploaded_by char(10)
);

CREATE TABLE csdl_bit.tags (
  id_tag char(10) PRIMARY KEY,
  name varchar(255)
);

CREATE TABLE csdl_bit.posts (
  id_post char(10) PRIMARY KEY,
  title text,
  content text,
  posted_by char(10)
);

CREATE TABLE csdl_bit.ratings (
  id_rating char(10) PRIMARY KEY,
  star_rating int,
  rated_by char(10),
  id_document char(10)
);

CREATE TABLE csdl_bit.comments (
  id_comment char(10) PRIMARY KEY,
  content text,
  commented_by char(10),
  id_document char(10),
  id_post char(10)
);

CREATE TABLE csdl_bit.posts_tags (
  id_post char(10),
  id_tag char(10),
  PRIMARY KEY (id_post, id_tag)
);

CREATE TABLE csdl_bit.documents_tags (
  id_document char(10),
  id_tag char(10),
  PRIMARY KEY (id_document, id_tag)
);

CREATE TABLE csdl_bit.Bookmarks (
  id_document char(10),
  id_user char(10),
  PRIMARY KEY (id_document, id_user)
);

ALTER TABLE csdl_bit.documents ADD FOREIGN KEY (uploaded_by) REFERENCES csdl_bit.users (id_user);

ALTER TABLE csdl_bit.posts ADD FOREIGN KEY (posted_by) REFERENCES csdl_bit.users (id_user);

ALTER TABLE csdl_bit.ratings ADD FOREIGN KEY (rated_by) REFERENCES csdl_bit.users (id_user);

ALTER TABLE csdl_bit.ratings ADD FOREIGN KEY (id_document) REFERENCES csdl_bit.documents (id_document);

ALTER TABLE csdl_bit.comments ADD FOREIGN KEY (commented_by) REFERENCES csdl_bit.users (id_user);

ALTER TABLE csdl_bit.comments ADD FOREIGN KEY (id_document) REFERENCES csdl_bit.documents (id_document);

ALTER TABLE csdl_bit.comments ADD FOREIGN KEY (id_post) REFERENCES csdl_bit.posts (id_post);

ALTER TABLE csdl_bit.posts_tags ADD FOREIGN KEY (id_post) REFERENCES csdl_bit.posts (id_post);

ALTER TABLE csdl_bit.posts_tags ADD FOREIGN KEY (id_tag) REFERENCES  csdl_bit.tags (id_tag);

ALTER TABLE csdl_bit.documents_tags ADD FOREIGN KEY (id_document) REFERENCES csdl_bit.documents (id_document);

ALTER TABLE csdl_bit.documents_tags ADD FOREIGN KEY (id_tag) REFERENCES  csdl_bit.tags (id_tag);

ALTER TABLE csdl_bit.Bookmarks ADD FOREIGN KEY (id_document) REFERENCES csdl_bit.documents (id_document);

ALTER TABLE csdl_bit.Bookmarks ADD FOREIGN KEY (id_user) REFERENCES csdl_bit.users (id_user);
