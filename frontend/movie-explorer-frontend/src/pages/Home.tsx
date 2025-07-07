
import React, { useEffect, useState } from 'react';
import api from '../services/api';

const Home = () => {
  const [movies, setMovies] = useState([]);
  const [genres, setGenres] = useState([]);
  const [directors, setDirectors] = useState([]);
  const [actors, setActors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // Filter and search states
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedGenre, setSelectedGenre] = useState('');
  const [selectedDirector, setSelectedDirector] = useState('');
  const [selectedActor, setSelectedActor] = useState('');
  const [sortBy, setSortBy] = useState('title');
  const [showFilters, setShowFilters] = useState(false);
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [favorites, setFavorites] = useState([]);
  const [watchLater, setWatchLater] = useState([]);

  // Load favorites and watch later from localStorage
  useEffect(() => {
    try {
      const savedFavorites = localStorage.getItem('movieFavorites');
      const savedWatchLater = localStorage.getItem('movieWatchLater');
      
      if (savedFavorites) {
        setFavorites(JSON.parse(savedFavorites));
      }
      if (savedWatchLater) {
        setWatchLater(JSON.parse(savedWatchLater));
      }
    } catch (e) {
      console.error('Error loading saved data:', e);
    }
  }, []);

  // Save favorites to localStorage
  useEffect(() => {
    try {
      localStorage.setItem('movieFavorites', JSON.stringify(favorites));
    } catch (e) {
      console.error('Error saving favorites:', e);
    }
  }, [favorites]);

  // Save watch later to localStorage
  useEffect(() => {
    try {
      localStorage.setItem('movieWatchLater', JSON.stringify(watchLater));
    } catch (e) {
      console.error('Error saving watch later:', e);
    }
  }, [watchLater]);

  // Fetch data
  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError(null);
      
      try {
        const [moviesRes, genresRes, directorsRes, actorsRes] = await Promise.all([
          api.get('movies/'),
          api.get('genres/'),
          api.get('directors/'),
          api.get('actors/')
        ]);
        
        setMovies(moviesRes.data);
        setGenres(genresRes.data);
        setDirectors(directorsRes.data);
        setActors(actorsRes.data);
        console.log(moviesRes);
      } catch (err) {
        setError('Failed to fetch data. Please try again.');
        console.error('Error fetching data:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Filter and sort movies
  const filteredMovies = movies
    .filter(movie => {
      const matchesSearch = movie.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          movie.director.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          movie.actors.some(actor => actor.name.toLowerCase().includes(searchTerm.toLowerCase()));
      
      const matchesGenre = !selectedGenre || movie.genres.some(genre => genre.name === selectedGenre);
      const matchesDirector = !selectedDirector || movie.director.name === selectedDirector;
      const matchesActor = !selectedActor || movie.actors.some(actor => actor.name === selectedActor);
      
      return matchesSearch && matchesGenre && matchesDirector && matchesActor;
    })
    .sort((a, b) => {
      switch (sortBy) {
        case 'title':
          return a.title.localeCompare(b.title);
        case 'year':
          return b.release_year - a.release_year;
        case 'rating':
          return b.rating - a.rating;
        default:
          return 0;
      }
    });

  const toggleFavorite = (movieId) => {
    setFavorites(prev => 
      prev.includes(movieId) 
        ? prev.filter(id => id !== movieId)
        : [...prev, movieId]
    );
  };

  const toggleWatchLater = (movieId) => {
    setWatchLater(prev => 
      prev.includes(movieId) 
        ? prev.filter(id => id !== movieId)
        : [...prev, movieId]
    );
  };

  const clearFilters = () => {
    setSearchTerm('');
    setSelectedGenre('');
    setSelectedDirector('');
    setSelectedActor('');
    setSortBy('title');
  };

  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      backgroundColor: '#f9fafb',
      minHeight: '100vh',
      margin: 0,
      padding: 0
    },
    header: {
      backgroundColor: '#ffffff',
      borderBottom: '1px solid #e5e7eb',
      padding: '1rem 2rem',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
    },
    title: {
      fontSize: '1.5rem',
      fontWeight: 'bold',
      color: '#1f2937',
      margin: 0,
      display: 'flex',
      alignItems: 'center'
    },
    titleIcon: {
      marginRight: '0.5rem',
      color: '#2563eb'
    },
    stats: {
      fontSize: '0.875rem',
      color: '#6b7280'
    },
    searchSection: {
      backgroundColor: '#ffffff',
      padding: '1.5rem 2rem',
      borderBottom: '1px solid #e5e7eb'
    },
    searchContainer: {
      display: 'flex',
      gap: '1rem',
      alignItems: 'center',
      flexWrap: 'wrap'
    },
    searchInput: {
      flex: 1,
      minWidth: '250px',
      padding: '0.75rem 1rem',
      border: '1px solid #d1d5db',
      borderRadius: '0.5rem',
      fontSize: '1rem',
      outline: 'none'
    },
    button: {
      padding: '0.75rem 1rem',
      backgroundColor: '#f3f4f6',
      border: '1px solid #d1d5db',
      borderRadius: '0.5rem',
      cursor: 'pointer',
      fontSize: '0.875rem',
      fontWeight: '500',
      transition: 'all 0.2s'
    },
    buttonHover: {
      backgroundColor: '#e5e7eb'
    },
    primaryButton: {
      backgroundColor: '#3A91ACFF',
      color: '#ffffff',
      border: 'none'
    },
    select: {
      padding: '0.75rem 1rem',
      border: '1px solid #d1d5db',
      borderRadius: '0.5rem',
      fontSize: '0.875rem',
      outline: 'none',
      backgroundColor: '#ffffff'
    },
    filtersPanel: {
      marginTop: '1rem',
      padding: '1rem',
      backgroundColor: '#f9fafb',
      border: '1px solid #e5e7eb',
      borderRadius: '0.5rem'
    },
    filtersGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
      gap: '1rem'
    },
    filterGroup: {
      display: 'flex',
      flexDirection: 'column'
    },
    label: {
      fontSize: '0.875rem',
      fontWeight: '500',
      marginBottom: '0.5rem',
      color: '#374151'
    },
    main: {
      padding: '2rem',
      maxWidth: '1200px',
      margin: '0 auto'
    },
    movieGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
      gap: '1.5rem'
    },
    movieCard: {
      backgroundColor: '#DAF2FDFF',
      borderRadius: '0.75rem',
      boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)',
      overflow: 'hidden',
      transition: 'transform 0.2s, box-shadow 0.2s'
    },
    movieCardHover: {
      transform: 'translateY(-2px)',
      boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)'
    },
    movieHeader: {
      padding: '1rem',
      borderBottom: '1px solid #e5e7eb'
    },
    movieTitle: {
      fontSize: '1.125rem',
      fontWeight: 'bold',
      margin: '0 0 0.5rem 0',
      color: '#1f2937'
    },
    movieMeta: {
      fontSize: '0.875rem',
      color: '#6b7280',
      marginBottom: '0.25rem'
    },
    movieContent: {
      padding: '1rem'
    },
    movieDescription: {
      fontSize: '0.875rem',
      color: '#4b5563',
      lineHeight: '1.5',
      marginBottom: '1rem'
    },
    genreList: {
      display: 'flex',
      flexWrap: 'wrap',
      gap: '0.5rem',
      marginBottom: '1rem'
    },
    genreTag: {
      backgroundColor: '#dbeafe',
      color: '#1e40af',
      padding: '0.25rem 0.75rem',
      borderRadius: '1rem',
      fontSize: '0.75rem',
      fontWeight: '500'
    },
    movieActions: {
      display: 'flex',
      gap: '0.5rem',
      marginTop: '1rem'
    },
    actionButton: {
      padding: '0.5rem 1rem',
      border: '1px solid #d1d5db',
      borderRadius: '0.5rem',
      cursor: 'pointer',
      fontSize: '0.875rem',
      backgroundColor: '#ffffff',
      display: 'flex',
      alignItems: 'center',
      gap: '0.5rem',
      transition: 'all 0.2s'
    },
    favoriteButton: {
      backgroundColor: '#dc2626',
      color: '#ffffff',
      border: 'none'
    },
    watchLaterButton: {
      backgroundColor: '#2563eb',
      color: '#ffffff',
      border: 'none'
    },
    modal: {
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.5)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 1000,
      padding: '1rem'
    },
    modalContent: {
      backgroundColor: '#ffffff',
      borderRadius: '0.75rem',
      maxWidth: '600px',
      width: '100%',
      maxHeight: '90vh',
      overflow: 'auto'
    },
    modalHeader: {
      padding: '1.5rem',
      borderBottom: '1px solid #e5e7eb',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center'
    },
    modalTitle: {
      fontSize: '1.25rem',
      fontWeight: 'bold',
      margin: 0
    },
    closeButton: {
      padding: '0.5rem',
      border: 'none',
      background: 'none',
      cursor: 'pointer',
      fontSize: '1.5rem',
      color: '#6b7280'
    },
    modalBody: {
      padding: '1.5rem'
    },
    loading: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      minHeight: '400px',
      fontSize: '1.125rem',
      color: '#6b7280'
    },
    error: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      minHeight: '400px',
      flexDirection: 'column',
      color: '#dc2626'
    },
    noResults: {
      textAlign: 'center',
      padding: '3rem',
      color: '#6b7280'
    }
  };

  if (loading) {
    return (
      <div style={styles.container}>
        <div style={styles.loading}>
          <div>Loading movies...</div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div style={styles.container}>
        <div style={styles.error}>
          <div>{error}</div>
          <button 
            style={{...styles.button, ...styles.primaryButton, marginTop: '1rem'}}
            onClick={() => window.location.reload()}
          >
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      {/* Header */}
      <header style={styles.header}>
        <h1 style={styles.title}>
          <span style={styles.titleIcon}>🎬</span>
          Movie Explorer
        </h1>
        <div style={styles.stats}>
          Favorites: {favorites.length} | Watch Later: {watchLater.length}
        </div>
      </header>

      {/* Search and Filters */}
      <div style={styles.searchSection}>
        <div style={styles.searchContainer}>
          <input
            type="text"
            placeholder="Search movies, directors, or actors..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={styles.searchInput}
          />
          
          <button
            onClick={() => setShowFilters(!showFilters)}
            style={styles.button}
          >
            🔍 Filters
          </button>
          
          <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
            style={styles.select}
          >
            <option value="title">Sort by Title</option>
            <option value="year">Sort by Year</option>
            <option value="rating">Sort by Rating</option>
          </select>
        </div>

        {showFilters && (
          <div style={styles.filtersPanel}>
            <div style={styles.filtersGrid}>
              <div style={styles.filterGroup}>
                <label style={styles.label}>Genre</label>
                <select
                  value={selectedGenre}
                  onChange={(e) => setSelectedGenre(e.target.value)}
                  style={styles.select}
                >
                  <option value="">All Genres</option>
                  {genres.map(genre => (
                    <option key={genre.id} value={genre.name}>{genre.name}</option>
                  ))}
                </select>
              </div>

              <div style={styles.filterGroup}>
                <label style={styles.label}>Director</label>
                <select
                  value={selectedDirector}
                  onChange={(e) => setSelectedDirector(e.target.value)}
                  style={styles.select}
                >
                  <option value="">All Directors</option>
                  {directors.map(director => (
                    <option key={director.id} value={director.name}>{director.name}</option>
                  ))}
                </select>
              </div>

              <div style={styles.filterGroup}>
                <label style={styles.label}>Actor</label>
                <select
                  value={selectedActor}
                  onChange={(e) => setSelectedActor(e.target.value)}
                  style={styles.select}
                >
                  <option value="">All Actors</option>
                  {actors.map(actor => (
                    <option key={actor.id} value={actor.name}>{actor.name}</option>
                  ))}
                </select>
              </div>
            </div>

            <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '1rem'}}>
              <button onClick={clearFilters} style={{...styles.button, color: '#2563eb'}}>
                Clear All Filters
              </button>
              <span style={{fontSize: '0.875rem', color: '#6b7280'}}>
                {filteredMovies.length} movie{filteredMovies.length !== 1 ? 's' : ''} found
              </span>
            </div>
          </div>
        )}
      </div>

      {/* Main Content */}
      <main style={styles.main}>
        {filteredMovies.length === 0 ? (
          <div style={styles.noResults}>
            <h3>No movies found</h3>
            <p>Try adjusting your search or filters</p>
            <button
              onClick={clearFilters}
              style={{...styles.button, ...styles.primaryButton, marginTop: '1rem'}}
            >
              Clear Filters
            </button>
          </div>
        ) : (
          <div style={styles.movieGrid}>
            {filteredMovies.map(movie => (
              <div key={movie.id} style={styles.movieCard}>
                <div style={styles.movieHeader}>
                  <h3 style={styles.movieTitle}>{movie.title}</h3>
                  <div style={styles.movieMeta}>
                    📅 {movie.release_year} • ⭐ {movie.rating} • ⏱️ {movie.duration} min
                  </div>
                  <div style={styles.movieMeta}>
                    🎬 {movie.director.name}
                  </div>
                </div>
                
                <div style={styles.movieContent}>
                  <p style={styles.movieDescription}>{movie.description}</p>
                  
                  <div style={styles.genreList}>
                    {movie.genres.map(genre => (
                      <span key={genre.id} style={styles.genreTag}>
                        {genre.name}
                      </span>
                    ))}
                  </div>
                  
                  <div style={styles.movieActions}>
                    <button
                      onClick={() => toggleFavorite(movie.id)}
                      style={{
                        ...styles.actionButton,
                        ...(favorites.includes(movie.id) ? styles.favoriteButton : {})
                      }}
                    >
                      ❤️ {favorites.includes(movie.id) ? 'Favorited' : 'Favorite'}
                    </button>
                    
                    <button
                      onClick={() => toggleWatchLater(movie.id)}
                      style={{
                        ...styles.actionButton,
                        ...(watchLater.includes(movie.id) ? styles.watchLaterButton : {})
                      }}
                    >
                      🕐 {watchLater.includes(movie.id) ? 'In List' : 'Watch Later'}
                    </button>
                    
                    <button
                      onClick={() => setSelectedMovie(movie)}
                      style={{...styles.actionButton, ...styles.primaryButton}}
                    >
                      👁️ View Details
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>

      {/* Movie Detail Modal */}
      {selectedMovie && (
        <div style={styles.modal} onClick={(e) => e.target === e.currentTarget && setSelectedMovie(null)}>
          <div style={styles.modalContent}>
            <div style={styles.modalHeader}>
              <h2 style={styles.modalTitle}>{selectedMovie.title}</h2>
              <button
                onClick={() => setSelectedMovie(null)}
                style={styles.closeButton}
              >
                ×
              </button>
            </div>
            
            <div style={styles.modalBody}>
              <div style={{marginBottom: '1rem'}}>
                <strong>Year:</strong> {selectedMovie.release_year}<br/>
                <strong>Rating:</strong> ⭐ {selectedMovie.rating}<br/>
                <strong>Duration:</strong> {selectedMovie.duration} minutes<br/>
                <strong>Director:</strong> {selectedMovie.director.name}
              </div>
              
              <div style={{marginBottom: '1rem'}}>
                <strong>Description:</strong>
                <p style={{marginTop: '0.5rem', lineHeight: '1.5'}}>{selectedMovie.description}</p>
              </div>
              
              <div style={{marginBottom: '1rem'}}>
                <strong>Cast:</strong>
                <div style={{marginTop: '0.5rem'}}>
                  {selectedMovie.actors.map(actor => (
                    <span key={actor.id} style={{...styles.genreTag, marginRight: '0.5rem', marginBottom: '0.5rem', display: 'inline-block'}}>
                      {actor.name}
                    </span>
                  ))}
                </div>
              </div>
              
              <div style={{marginBottom: '1rem'}}>
                <strong>Genres:</strong>
                <div style={{marginTop: '0.5rem'}}>
                  {selectedMovie.genres.map(genre => (
                    <span key={genre.id} style={{...styles.genreTag, marginRight: '0.5rem', marginBottom: '0.5rem', display: 'inline-block'}}>
                      {genre.name}
                    </span>
                  ))}
                </div>
              </div>
              
              <div style={styles.movieActions}>
                <button
                  onClick={() => toggleFavorite(selectedMovie.id)}
                  style={{
                    ...styles.actionButton,
                    ...(favorites.includes(selectedMovie.id) ? styles.favoriteButton : {})
                  }}
                >
                  ❤️ {favorites.includes(selectedMovie.id) ? 'Remove from Favorites' : 'Add to Favorites'}
                </button>
                
                <button
                  onClick={() => toggleWatchLater(selectedMovie.id)}
                  style={{
                    ...styles.actionButton,
                    ...(watchLater.includes(selectedMovie.id) ? styles.watchLaterButton : {})
                  }}
                >
                  🕐 {watchLater.includes(selectedMovie.id) ? 'Remove from Watch Later' : 'Add to Watch Later'}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Home;