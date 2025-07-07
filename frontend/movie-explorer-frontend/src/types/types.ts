export interface MovieType {
  id: number;
  title: string;
  release_year: number;
  director: { name: string };
  genres: { name: string }[];
}

export interface PaginatedResponse {
  movies: MovieType[];
  total_pages: number;
}
